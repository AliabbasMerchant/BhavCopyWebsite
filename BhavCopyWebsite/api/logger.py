import logging
from datetime import datetime
from pathlib import Path

logger = logging.getLogger("bhavcopy")
logger.propagate = False
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s", "%b %d %H:%M:%S")

LOG_DIR = f"{Path(__file__).resolve().parent.parent}/logs"
file_handler = logging.FileHandler(f"{LOG_DIR}/{datetime.strftime(datetime.now(), '%b %d %H:%M:%S')}.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
