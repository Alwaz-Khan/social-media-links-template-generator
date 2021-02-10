import time

from supbot import Supbot

title = ""
linkedin_url = ""
twitter_url = ""
facebook_url = ""
instagram_url = ""

stop_execution = False
forward_group_list = ["Alwaz Khan", "Nutty gang"]
consolidated_message = ""
sponsorship_ad = """
Powered by Supbot2
https://adsau59.github.io/Supbot2/
"""

linkedin_template = "*LinkedIn*\n{}\n"
twitter_template = "*Twitter*\n{}\n"
instagram_template = "*Instagram*\n{}\n"
facebook_template = "*Facebook*\n{}\n"


def message_received(group_name: str, contact_name: str, message: str):
    global title, linkedin_url, twitter_url, facebook_url, instagram_url, consolidated_message, stop_execution
    if not (group_name == "sirf juniors" or group_name == "Nutty gang"):
        return
    if "supbot2 hi" in message.lower():
        supbot.send_message(group_name, "Supbot Online")

    if "supbot2 help" in message.lower():
        help(group_name)

    if "supbot2 title" in message.lower():
        split_message = message.split("le\n")
        title = ""
        try:
            for line in split_message[1].split("\n"):
                title += "*" + line + "*\n"
            if not (linkedin_url and twitter_url and facebook_url and instagram_url):
                supbot.send_message(group_name, "Waiting for links")
        except IndexError:
            supbot.send_message(group_name, "Please Input Title with correct format")

    if "linkedin.com/" in message:
        linkedin_url = message
        if not (linkedin_url and twitter_url and facebook_url and instagram_url):
            supbot.send_message(group_name, "LinkedIn link received")
        send_title(group_name)

    elif "twitter.com/" in message:
        twitter_url = message
        if not (linkedin_url and twitter_url and facebook_url and instagram_url):
            supbot.send_message(group_name, "Twitter link received")
        send_title(group_name)

    elif "facebook.com/" in message:
        facebook_url = message
        if not (title and linkedin_url and twitter_url and facebook_url and instagram_url):
            supbot.send_message(group_name, "Facebook link received")
        send_title(group_name)

    elif "instagram.com/" in message:
        instagram_url = message
        if not (linkedin_url and twitter_url and facebook_url and instagram_url):
            supbot.send_message(group_name, "Instagram link received")
        send_title(group_name)

    if "supbot2 stop" in message.lower():
        stop_execution = True

    if (title and linkedin_url and twitter_url and facebook_url and instagram_url) or "supbot2 publish" in message:
        consolidated_message = prepare_consolidated_message()
        supbot.send_message(group_name, consolidated_message)
        supbot.send_message(group_name, sponsorship_ad)
        stop_execution = False
        supbot.send_message(group_name, "Forwarding to other groups in 5 minutes")
        time.sleep(20)
        supbot.send_message(group_name, "Forwarding in 1 minute")
        time.sleep(20)
        if not stop_execution:
            supbot.send_message(group_name, "Message Forwarded")
            for name in forward_group_list:
                supbot.send_message(name, consolidated_message)
            clear_title()
            clear_links()
        if stop_execution:
            clear_links()
            supbot.send_message("Waiting for new links")


def send_title(group_name):
    if not title:
        supbot.send_message(group_name, "Please provide title too.")


def help(group_name):
    supbot.send_message(group_name, "*Commands Available*\n\n```supbot2 hi```\nChecks if I am sleep or awake.\n\n"
                                    "```supbot2 title```\nwrite the caption/title of the post on the next line, "
                                    "in the same message\n\n_Example_\nsupbot2 title\nTeam CommPR\n2020-2022\n\n"
                                    "```supbot2 publish```\npubllish the tempate with the available links")


def prepare_consolidated_message():
    global title, linkedin_url, twitter_url, facebook_url, instagram_url
    message = title + "\n"
    if linkedin_url:
        message += "\n" + linkedin_template.format(linkedin_url)
    if twitter_url:
        message += "\n" + twitter_template.format(twitter_url)
    if facebook_url:
        message += "\n" + facebook_template.format(facebook_url)
    if instagram_url:
        message += "\n" + instagram_template.format(instagram_url)
    return message


def clear_title():
    global title
    title = ""


def clear_links():
    global linkedin_url, twitter_url, facebook_url, instagram_url
    linkedin_url = ""
    twitter_url = ""
    facebook_url = ""
    instagram_url = ""


with Supbot(group_message_received=message_received) as supbot:
    supbot.wait_for_finish()
