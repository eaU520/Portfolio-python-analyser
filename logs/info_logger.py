import logging
import os
from logging.handlers import RotatingFileHandler

info_file = "../Portfolio-python-analyser/logs/analyser_logs.log"

def initialize_logger():
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename=info_file, level=logging.INFO, format="%(asctime)s - %(name)s - %(message)s",force=True)
    logger.info('Info Logging starting')
    
    handler = RotatingFileHandler(info_file, mode="w", backupCount=5)#TODO: Make configurable
    logger.addHandler(handler)
    if os.path.isfile(info_file):
        handler.doRollover()
    return logger
