import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path

#info_file = "../Portfolio-python-analyser/logs/analyser_logs.log"
info_file = "./logs/analyser_logs.log"

def initialize_logger():
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename=info_file, level=logging.INFO, format="%(asctime)s - %(name)s - %(message)s",force=True)
    logger.info('Info Logging starting')
    
    handler = RotatingFileHandler(info_file, mode="w")#TODO: Make configurable
    logger.addHandler(handler)
    if os.path.isfile(info_file):
        handler.doRollover()
    return logger
