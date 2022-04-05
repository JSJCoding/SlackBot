from config import slack_config
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

SETTINGS = slack_config()
CLIENT = WebClient(token=SETTINGS["slack_token"])


def post_message(channel, message):
    try:
        response = CLIENT.chat_postMessage(
            channel=channel,
            text=f"{message}"
        )
    except SlackApiError as e:
        assert e.response['error']

    return response


def post_thread(channel, timestamp, message):
    try:
        response = CLIENT.chat_postMessage(
            channel=channel,
            thread_ts=f"{timestamp}",
            text=f"{message}"
        )
    except SlackApiError as e:
        assert e.response['error']

    return response


def post_update(channel, timestamp, message):
    try:
        response = CLIENT.chat_update(
            channel=channel,
            ts=f"{timestamp}",
            text=f"{message}"
        )
    except SlackApiError as e:
        assert e.response['error']

    return response
