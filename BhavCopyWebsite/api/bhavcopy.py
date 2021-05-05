from typing import Optional
import requests
from datetime import date, timedelta
import os
import zipfile
import redis
import csv
from dotenv import load_dotenv
from pathlib import Path

from .logger import logger

DATA_DIR = f"{Path(__file__).resolve().parent.parent}/data"

CSV_TO_REDIS_KEY_MAPPING = {
    'SC_CODE': 'code',
    'SC_NAME': 'name',
    'OPEN': 'open',
    'HIGH': 'high',
    'LOW': 'low',
    'CLOSE': 'close',
}


def download_bhavcopy_zip(date_string: str, zip_save_path: str) -> bool:
    # Download the zip for the current date
    url = f"https://www.bseindia.com/download/BhavCopy/Equity/EQ{date_string}_CSV.ZIP"
    r = requests.get(url, stream=True, headers={
        # does not work without a valid User-Agent
        'User-Agent': 'PostmanRuntime/7.26.8'
    })
    if r.status_code != 200:
        # the file is not available
        # the market may be closed
        return False
    with open(zip_save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=16):
            fd.write(chunk)
    return True


def extract_zip_and_delete_it(zip_file_path: str, dir_to_extract_to: str):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(dir_to_extract_to)
    os.remove(zip_file_path)


def ingest_csv(csv_path):
    load_dotenv()

    redis_instance = redis.StrictRedis(host=os.getenv(
        'REDIS_HOST'), port=os.getenv('REDIS_PORT'), db=os.getenv('REDIS_DB'))

    with open(csv_path, 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            row = dict(row)
            redis_data = {}
            for csv_key in CSV_TO_REDIS_KEY_MAPPING:
                redis_key = CSV_TO_REDIS_KEY_MAPPING[csv_key]
                redis_data[redis_key] = row[csv_key].strip()
            hset_key = redis_data['name']
            redis_data.pop('name')
            redis_instance.hset(hset_key, mapping=redis_data)


def download_and_ingest(date_string: Optional[str] = None) -> bool:
    if date_string is None:
        date_string = date.today().strftime("%d%m%y")

    zip_file_path = f"{DATA_DIR}/{date_string}.zip"
    if not os.path.exists(DATA_DIR):
        os.mkdir(DATA_DIR)

    logger.debug(f"Attempting to download zip for date {date_string} to file {zip_file_path}...")
    zip_was_downloaded = download_bhavcopy_zip(date_string, zip_file_path)
    if not zip_was_downloaded:
        logger.debug("Zip not downloaded")
        return False
    logger.debug("Zip downloaded")

    extract_zip_and_delete_it(zip_file_path, DATA_DIR)

    csv_path = f"{DATA_DIR}/EQ{date_string}.CSV"
    logger.debug(f"CSV {csv_path} extracted from the zip")

    ingest_csv(csv_path)
    logger.debug(f"CSV {csv_path} ingested")
    return True


def init_data():
    # if there is no data in Redis, try to pull in the latest data
    load_dotenv()

    redis_instance = redis.StrictRedis(host=os.getenv(
        'REDIS_HOST'), port=os.getenv('REDIS_PORT'), db=os.getenv('REDIS_DB'))
    if redis_instance.hgetall('HDFC') is None: # Some random company
        # there is no data
        d = date.today()
        while True:
            if download_and_ingest(date_string=d.strftime("%d%m%y")):
                break
            d = d - timedelta(days=1)


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        date_string = sys.argv[1]
        assert len(date_string) == 6
        assert date_string.isnumeric()
        # basic asserts, no need for more as such
    else:
        date_string = "300421"
    print(f"Will download and ingest BhavCopy data of date {date_string}")
    ok = download_and_ingest(date_string=date_string)
    print("Operation successful" if ok else "Could not get data")
