import logging

def initialize_logger():
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='../Portfolio-python-analyser/logs/data.log', level=logging.INFO)
    logger.info('Started')
    logger.info('Finished')
    return logger
