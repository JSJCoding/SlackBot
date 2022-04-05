import configparser

CONFIG = None


def read_config():
    global CONFIG
    if CONFIG is None:
        CONFIG = configparser.ConfigParser()
        CONFIG.read("config.ini")


def conn_config():
    read_config()
    return {
            "path": "xxxx",
            }


def slack_config():
    read_config()
    return {
            "debug": CONFIG.get("slack", "debug", fallback=True),
            "slack_token": CONFIG.get("slack", "token", fallback=""),
            "channel_id": CONFIG.get("slack", "channel_id", fallback=""),
            "channels": {
                    "test": "xxxx"
                }
    }
