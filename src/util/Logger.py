import logging
import os
from pathlib import Path

from src import settings

ROOT_DIR = os.path.dirname(Path(__file__).parent.parent.parent)
LOG_DIR = os.path.join(ROOT_DIR, "test-output", "logs")
print("LOG FILE PATH : " + LOG_DIR + settings.LOG_FILE)


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=LOG_DIR + settings.LOG_FILE,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
