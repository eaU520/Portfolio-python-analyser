import json
def import_json(file_name):
    default_config = json.load(file_name)
    return default_config