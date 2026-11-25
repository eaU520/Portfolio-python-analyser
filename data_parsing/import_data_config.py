import json
import logging
logger_info = logging.getLogger("logs.info_logger")
def import_json(file_name):
    default_config = json.load(file_name)
    logger_info.info("Importing default configs")
    return default_config