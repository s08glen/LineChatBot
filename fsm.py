from transitions.extensions import GraphMachine


from utils import send_text_message, send_image_url,send_template
from linebot.models import MessageEvent, PostbackEvent, TextSendMessage, TemplateSendMessage, ButtonsTemplate,PostbackTemplateAction, MessageTemplateAction, URITemplateAction,ImageSendMessage


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_user(self, event):
        text = event.message.text
        return text.lower() == "go to user"

    def is_going_to_life(self, event):
        text = event.message.text
        return text.lower() == "go to life"

    def is_going_to_nowgood(self, event):
        text = event.message.text
        return text.lower() == "go to nowgood"

    def is_going_to_votenowagain(self, event):
        text = event.message.text
        return text.lower() == "go to votenowagain"

    def is_going_to_nowthank(self, event):
        text = event.message.text
        return text.lower() == "go to nowthank"
		
    def is_going_to_chooseanother(self, event):
        text = event.message.text
        return text.lower() == "go to chooseanother"
		
    def is_going_to_kp(self, event):
        text = event.message.text
        return text.lower() == "go to kp"
	
    def is_going_to_votehan(self, event):
        text = event.message.text
        return text.lower() == "go to votehan"

    def is_going_to_voteorange(self, event):
        text = event.message.text
        return text.lower() == "go to voteorange"
	
    def is_going_to_orangethank(self, event):
        text = event.message.text
        return text.lower() == "go to orangethank"
	
    def is_going_to_u87(self, event):
        text = event.message.text
        return text.lower() == "go to u87"



    def on_enter_user(self, event):
        user_id = event.source.user_id
        print(user_id)
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
                title='Start',
                text='User',
                thumbnail_image_url='https://i.imgur.com/mjUakr3.jpg',
                actions=[
                    MessageTemplateAction(
                        label='Go',
                        text='go to life'
                    ),
                ]
            )
        )
        reply_token = event.reply_token
        #push_template(id,buttons_template)
        send_template(reply_token, buttons_template)

    def on_enter_life(self, event):
        user_id = event.source.user_id
        print(user_id)
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
                title='Life',
                text='你覺得現在經濟生活過得如何??',
                thumbnail_image_url='https://i.imgur.com/mjUakr3.jpg',
                actions=[
                    MessageTemplateAction(
                        label='go to nowgood',
                        text='go to nowgood'
                    ),
                    MessageTemplateAction(
                        label='go to votehh',
                        text='go to votehan'
                    ),
                ]
            )
        )
        reply_token = event.reply_token
        #push_template(id,buttons_template)
        send_template(reply_token, buttons_template)


    def on_enter_nowgood(self, event):
        user_id = event.source.user_id
        print(user_id)
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
                title='Now Good?',
                text='現任總統蔡英文做得好嗎??',
                thumbnail_image_url='https://i.imgur.com/mjUakr3.jpg',
                actions=[
                    MessageTemplateAction(
                        label='好',
                        text='go to votenowagain'
                    ),
                    MessageTemplateAction(
                        label='不好',
                        text='go to chooseanother'
                    ),
                ]
            )
        )
        reply_token = event.reply_token
        #push_template(id,buttons_template)
        send_template(reply_token, buttons_template)



        '''
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger nowgood")
        '''

    def on_enter_votenowagain(self, event):
        user_id = event.source.user_id
        print(user_id)
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
                title='Vote now again?',
                text='你會再投連任嗎??',
                thumbnail_image_url='https://i.imgur.com/mjUakr3.jpg',
                actions=[
                    MessageTemplateAction(
                        label='會',
                        text='go to nowthank'
                    ),
                    MessageTemplateAction(
                        label='不會',
                        text='go to chooseanother'
                    ),
                ]
            )
        )
        reply_token = event.reply_token
        #push_template(id,buttons_template)
        send_template(reply_token, buttons_template)

    def on_enter_nowthank(self, event):
        user_id = event.source.user_id
        print(user_id)
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
                title='Thank you',
                text='小瑛感謝你??',
                thumbnail_image_url='https://i.imgur.com/mjUakr3.jpg',
                actions=[
                    MessageTemplateAction(
                        label='回到一開始',
                        text='go to user'
                    ),
                ]
            )
        )
        reply_token = event.reply_token
        #push_template(id,buttons_template)
        send_template(reply_token, buttons_template)

    def on_enter_chooseanother(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger choose another")

    def on_enter_kp(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger Kp didn't add")

    def on_enter_votehan(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger vote han")

    def on_enter_voteorange(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger vote orange")

    def on_enter_orangethank(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger orange thank")

    def on_enter_u87(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger u87")


'''
    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")
'''