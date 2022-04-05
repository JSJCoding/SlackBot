import slack
from config import filepath_config
from datetime import date, timedelta


SETTINGS = filepath_config()
PATH = SETTINGS['filepath']


def get_keycode(today):
    new_code = old_code = None
    with open(PATH) as keyfile:
        for key in keyfile:
            date, recipient, sender, subject, code = key.split('|')
            if date == str(today):
                code = code.split(';')
                new_code = ''.join(filter(str.isdigit, code[0]))
                old_code = ''.join(filter(str.isdigit, code[1]))

    return new_code, old_code


next_post = today = date.today()
if next_post != today:
    slack.post_message("#test", "There shall be no post today!")
    exit()

new_code, old_code = get_keycode(today)
if new_code is None or old_code is None:
    new_code, old_code = get_keycode(today-timedelta(today.isoweekday()))
    slack.post_message(
            "#test", f"No keys for today the old code is: {old_code}")
    exit()

slack.post_message(
        "#test", f"Havne keys has been updated: \n {old_code} -> {new_code}")

next_post += timedelta(days=7)
