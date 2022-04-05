import configparser

CONFIG = None


def read_config():
    global CONFIG
    if CONFIG is None:
        CONFIG = configparser.ConfigParser()
        CONFIG.read("config.ini")


def filepath_config():
    read_config()
    return {
            "filepath": CONFIG.get("default", "key_filepath", fallback=""),
            }


def slack_config():
    read_config()
    return {
            "debug": CONFIG.get("default", "debug", fallback=True),
            "slack_token": CONFIG.get("default", "token", fallback=""),
            "channel_id": CONFIG.get("default", "channel_id", fallback=""),
    }
