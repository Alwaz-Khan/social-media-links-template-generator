from supbot import Supbot

title = ""
linkedin_url = ""
twitter_url = ""
facebook_url = ""
instagram_url = ""

sponsorship_ad = """
Powered by Supbot2
https://adsau59.github.io/Supbot2/
"""

linkedin_template = "*LinkedIn*\n{}\n"
twitter_template = "*Twitter*\n{}\n"
instagram_template = "*Instagram*\n{}\n"
facebook_template = "*Facebook*\n{}\n"


def message_received(group_name: str, contact_name: str, message: str):
    global title, linkedin_url, twitter_url, facebook_url, instagram_url
    if not (group_name == "sirf juniors" or group_name == "Nutty gang"):
        return
    if "supbot2 hi" in message.lower():
        supbot.send_message(group_name, "Supbot Online")

    if "supbot2 help" in message.lower():
        help(group_name)

    if "supbot2 title" in message.lower():
        split_message = message.split("le\n")
        title = ""
        for line in split_message[1].split("\n"):
            title += "*" + line + "*\n"
        if not (linkedin_url and twitter_url and facebook_url and instagram_url):
            supbot.send_message(group_name, "Waiting for links")

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

    if (title and linkedin_url and twitter_url and facebook_url and instagram_url) or "supbot2 publish" in message:
        send_consolidated_message = consolidated_message()
        supbot.send_message(group_name, send_consolidated_message)
        supbot.send_message(group_name, sponsorship_ad)

def send_title(group_name):
    if not title:
        supbot.send_message(group_name, "Please provide title too.")

def help(group_name):
    supbot.send_message(group_name, "*Commands Available*\n\n```supbot2 hi```\nChecks if I am sleep or awake.\n\n"
                                    "```supbot2 title```\nwrite the caption/title of the post on the next line, "
                                    "in the same message\n\n_Example_\nsupbot2 title\nTeam CommPR\n2020-2022\n\n"
                                    "```supbot2 publish```\npubllish the tempate with the available links")

def consolidated_message():
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

    title = ""
    linkedin_url = ""
    twitter_url = ""
    facebook_url = ""
    instagram_url = ""
    return message


with Supbot(group_message_received=message_received) as supbot:
    supbot.wait_for_finish()