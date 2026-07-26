import json
def load_config():
    with open("./config.json") as file:
        config_file = file.read()
        config = json.loads(config_file)
    class Config:
        entries_db_path = config["entries_db_path"]
        users_db_path = config["users_db_path"]
    config_obj = Config()
    return config_obj