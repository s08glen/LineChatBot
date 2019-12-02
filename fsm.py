from transitions.extensions import GraphMachine


from utils import send_text_message, send_image_url
from linebot.models import MessageEvent, PostbackEvent, TextSendMessage, TemplateSendMessage,
                            TextMessage, ButtonsTemplate,PostbackTemplateAction, MessageTemplateAction, URITemplateAction,ImageSendMessage


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

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


    def on_enter_life(self, event):
        pass

    def on_enter_nowgood(self, event):
        pass

    def on_enter_votenowagain(self, event):
        pass

    def on_enter_nowthank(self, event):
        pass

    def on_enter_chooseanother(self, event):
        pass

    def on_enter_kp(self, event):
        pass

    def on_enter_votehan(self, event):
        pass

    def on_enter_voteorange(self, event):
        pass

    def on_enter_orangethank(self, event):
        pass

    def on_enter_u87(self, event):
        pass


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