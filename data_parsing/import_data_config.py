import json
import logging
logger_info = logging.getLogger("logs.info_logger")
def import_json(file_name):
    with open(file_name, 'r') as file:
        default_config = json.load(file)
        logger_info.info("Importing default configs")
    return default_config