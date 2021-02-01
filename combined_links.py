from supbot import Supbot

bot_called = False
title = ""
linkedin_url = ""
twitter_url = ""
facebook_url = ""
instagram_url = ""
template = """{} 

*LinkedIn*
{}

*Twitter*
{}

*Facebook*
{}

*Instagram*
{}"""

sponsorship_ad = """
Powered by Supbot2
https://adsau59.github.io/Supbot2/
"""


def message_received(group_name: str, contact_name: str, message: str):
    global bot_called, title, linkedin_url, twitter_url, facebook_url, instagram_url
    if not (group_name == "sirf juniors" or group_name == "Nutty gang"):
        return
    if "supbot2 hi" in message.lower():
        supbot.send_message(group_name, "Supbot Online")
    if "supbot2 title" in message.lower():
        supbot.send_message(group_name, "Waiting for links")
        split_message = message.split("le\n")
        title = ""
        for line in split_message[1].split("\n"):
            title += "*" + line + "*\n"
        bot_called = True
        return

    if "linkedin.com/" in message:
        linkedin_url = message
        if not title:
            supbot.send_message(group_name, "Please Mention post title first")
        elif not (title and linkedin_url and twitter_url and facebook_url and instagram_url):
            supbot.send_message(group_name, "LinkedIn link received")

    elif "twitter.com/" in message:
        twitter_url = message
        if not title:
            supbot.send_message(group_name, "Please Mention post title first")
        elif not (title and linkedin_url and twitter_url and facebook_url and instagram_url):
            supbot.send_message(group_name, "Twitter link received")

    elif "facebook.com/" in message:
        facebook_url = message
        if not title:
            supbot.send_message(group_name, "Please Mention post title first")
        elif not (title and linkedin_url and twitter_url and facebook_url and instagram_url):
            supbot.send_message(group_name, "Facebook link received")

    elif "instagram.com/" in message:
        instagram_url = message
        if not title:
            supbot.send_message(group_name, "Please Mention post title first")
        elif not (title and linkedin_url and twitter_url and facebook_url and instagram_url):
            supbot.send_message(group_name, "Instagram link received")

    if (title and linkedin_url and twitter_url and facebook_url and instagram_url) or "supbot2 publish" in message:
        send_consolidated_message = consolidated_message()
        supbot.send_message(group_name, send_consolidated_message)
        supbot.send_message(group_name, sponsorship_ad)


def consolidated_message():
    global bot_called, title, linkedin_url, twitter_url, facebook_url, instagram_url
    message = template.format(title, linkedin_url, twitter_url, facebook_url, instagram_url)
    bot_called = False
    title = ""
    linkedin_url = ""
    twitter_url = ""
    facebook_url = ""
    instagram_url = ""
    return message


with Supbot(group_message_received=message_received) as supbot:
    supbot.wait_for_finish()