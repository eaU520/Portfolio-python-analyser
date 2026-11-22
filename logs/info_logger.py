import logging

def initialize_logger():
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='../Portfolio-python-analyser/logs/analyser_logs.log', level=logging.INFO)
    logger.info('Logging started at ')
    return logger
