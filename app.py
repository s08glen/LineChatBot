import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()


machine = TocMachine(
    states=["user", "life", "nowgood","votenowagain","nowthank",
        "chooseanother","kp","votehan","voteorange","orangethank","u87"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "life",
            "conditions": "is_going_to_life",
        },
		{
            "trigger": "advance",
            "source": "life",
            "dest": "nowgood",
            "conditions": "is_going_to_nowgood",
        },
		{
            "trigger": "advance",
            "source": "life",
            "dest": "votehan",
            "conditions": "is_going_to_votehan",
        },
		{
            "trigger": "advance",
            "source": "nowgood",
            "dest": "votenowagain",
            "conditions": "is_going_to_votenowagain",
        },
		{
            "trigger": "advance",
            "source": "nowgood",
            "dest": "chooseanother",
            "conditions": "is_going_to_chooseanother",
        },
		{
            "trigger": "advance",
            "source": "votenowagain",
            "dest": "chooseanother",
            "conditions": "is_going_to_chooseanother",
        },
		{
            "trigger": "advance",
            "source": "chooseanother",
            "dest": "votenowagain",
            "conditions": "is_going_to_votenowagain",
        },
		{
            "trigger": "advance",
            "source": "chooseanother",
            "dest": "kp",
            "conditions": "is_going_to_kp",
        },
		{
            "trigger": "advance",
            "source": "kp",
            "dest": "chooseanother",
            "conditions": "is_going_to_chooseanother",
        },
		{
            "trigger": "advance",
            "source": "chooseanother",
            "dest": "votehan",
            "conditions": "is_going_to_votehan",
        },
		{
            "trigger": "advance",
            "source": "chooseanother",
            "dest": "voteorange",
            "conditions": "is_going_to_voteorange",
        },
		{
            "trigger": "advance",
            "source": "votehan",
            "dest": "voteorange",
            "conditions": "is_going_to_voteorange",
        },
		{
            "trigger": "advance",
            "source": "voteorange",
            "dest": "votenowagain",
            "conditions": "is_going_to_votenowagain",
        },
		{
            "trigger": "advance",
            "source": "voteorange",
            "dest": "orangethank",
            "conditions": "is_going_to_orangethank",
        },
		{
            "trigger": "advance",
            "source": "votenowagain",
            "dest": "nowthank",
            "conditions": "is_going_to_nowthank",
        },
		{
            "trigger": "advance",
            "source": "votehan",
            "dest": "u87",
            "conditions": "is_going_to_u87",
        },
        {
            "trigger": "advance",
            "source": "u87",
            "dest": "user",
            "conditions": "is_going_to_user",
        },
        {
            "trigger": "advance",
            "source": "orangethank",
            "dest": "user",
            "conditions": "is_going_to_user",
        },
        {
            "trigger": "advance",
            "source": "nowthank",
            "dest": "user",
            "conditions": "is_going_to_user",
        },
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)
handler = WebhookHandler(channel_secret)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # get user id when reply
    user_id = event.source.user_id
    print("user_id =", user_id)

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "Not Entering any State")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
