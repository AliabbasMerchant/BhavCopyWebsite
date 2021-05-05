import logging
from datetime import datetime

logger = logging.getLogger("bhavcopy")
logger.propagate = False
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s", "%b %d %H:%M:%S")

file_handler = logging.FileHandler("log/" + datetime.strftime(datetime.now(), "%b %d %H:%M:%S") + ".log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
