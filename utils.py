import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.models import MessageEvent, PostbackEvent, TextSendMessage, TemplateSendMessage, TextMessage, ButtonsTemplate,PostbackTemplateAction, MessageTemplateAction, URITemplateAction,ImageSendMessage


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"



def send_image_url(id, img_url):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.push_message(id, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
    return "OK"


def send_template(reply_token,template):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, template)
    return "OK"

def send_template_withtext(reply_token,template,text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, [template,TextSendMessage(text=text)])
    return "OK"
'''
def push_template(id,message):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.push_message(id, message)
    return "OK"
'''


"""
def send_button_message(id, text, buttons):
    pass
"""
