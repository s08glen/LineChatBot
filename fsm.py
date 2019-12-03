from transitions.extensions import GraphMachine


from utils import send_text_message, send_image_url,send_template
from linebot.models import MessageEvent, PostbackEvent, TextSendMessage, TemplateSendMessage, ButtonsTemplate,PostbackTemplateAction, MessageTemplateAction, URITemplateAction,ImageSendMessage


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_user(self, event):
        text = event.message.text
        return (text.lower() == "go to user" or text.lower() == "回到一開始" or text.lower() == "好" or text.lower() == "Go")

    def is_going_to_life(self, event):
        text = event.message.text
        return (text.lower() == "go to life" or text.lower() == "Go")

    def is_going_to_nowgood(self, event):
        text = event.message.text
        return (text.lower() == "go to nowgood" or text.lower() == "普通" or text.lower() == "好")

    def is_going_to_votenowagain(self, event):
        text = event.message.text
        return (text.lower() == "go to votenowagain" or text.lower() == "好" or text.lower() == "小英" or text.lower() == "No" )

    def is_going_to_nowthank(self, event):
        text = event.message.text
        return ( text.lower() == "go to nowthank" or text.lower() == "會" )
		
    def is_going_to_chooseanother(self, event):
        text = event.message.text
        return ( text.lower() == "go to chooseanother" or text.lower() == "不好" or text.lower() == "不會" or text.lower() == "回去再選一次" or text.lower() == "No")
		
    def is_going_to_kp(self, event):
        text = event.message.text
        return ( text.lower() == "go to kp" or text.lower() == '柯文哲')
	
    def is_going_to_votehan(self, event):
        text = event.message.text
        return ( text.lower() == "go to votehan" or text.lower() == "不好" or text.lower() == "韓導")

    def is_going_to_voteorange(self, event):
        text = event.message.text
        return ( text.lower() == "go to voteorange" or text.lower() == "宋楚瑜" or text.lower() == "不會")
	
    def is_going_to_orangethank(self, event):
        text = event.message.text
        return ( text.lower() == "go to orangethank" or text.lower() == '好' )
	
    def is_going_to_u87(self, event):
        text = event.message.text
        return (text.lower() == "go to u87" or text.lower() == "會")



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
                        label='好',
                        text='好'
                    ),
                    MessageTemplateAction(
                        label='普通',
                        text='普通'
                    ),
                    MessageTemplateAction(
                        label='不好',
                        #text='go to votehan'
                        text='不好'
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
                thumbnail_image_url='https://i.imgur.com/IQdilw0.jpg',
                actions=[
                    MessageTemplateAction(
                        label='好',
                        text='好'
                    ),
                    MessageTemplateAction(
                        label='不好',
                        text='不好'
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
                thumbnail_image_url='https://i.imgur.com/1UGnv0W.jpg',
                actions=[
                    MessageTemplateAction(
                        label='會',
                        text='會'
                    ),
                    MessageTemplateAction(
                        label='不會',
                        text='不會'
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
                text='小英感謝你?',
                thumbnail_image_url='https://i.imgur.com/gWUraP3.jpg',
                actions=[
                    MessageTemplateAction(
                        label='回到一開始',
                        text='回到一開始'
                    ),
                ]
            )
        )
        reply_token = event.reply_token
        #push_template(id,buttons_template)
        send_template(reply_token, buttons_template)

    def on_enter_chooseanother(self, event):
        user_id = event.source.user_id
        print(user_id)
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
                title='Vote now again?',
                text='那這些人要支持誰',
                thumbnail_image_url='https://i.imgur.com/mjUakr3.jpg',
                actions=[
                    MessageTemplateAction(
                        label='柯文哲',
                        text='柯文哲'
                    ),
                    MessageTemplateAction(
                        label='小英',
                        text='小英'
                    ),
                    MessageTemplateAction(
                        label='韓導',
                        text='韓導'
                    ),
                    MessageTemplateAction(
                        label='宋楚瑜',
                        text='宋楚瑜'
                    ),
                ]
            )
        )
        reply_token = event.reply_token
        #push_template(id,buttons_template)
        send_template(reply_token, buttons_template)

    def on_enter_kp(self, event):
        user_id = event.source.user_id
        print(user_id)
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
                title='額....',
                text='他沒參選總統捏',
                thumbnail_image_url='https://i.imgur.com/zpWkQqn.jpg',
                actions=[
                    MessageTemplateAction(
                        label='回去再選一次',
                        text='回去再選一次'
                    ),
                ]
            )
        )
        reply_token = event.reply_token
        #push_template(id,buttons_template)
        send_template(reply_token, buttons_template)

    def on_enter_votehan(self, event):
        user_id = event.source.user_id
        print(user_id)
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
                title='Vote Han',
                text='2020大選你會投給韓國瑜嗎?',
                thumbnail_image_url='https://i.imgur.com/bi6SDgg.jpg',
                actions=[
                    MessageTemplateAction(
                        label='會',
                        text='會'
                    ),
                    MessageTemplateAction(
                        label='不會',
                        text='不會'
                    ),
                ]
            )
        )
        reply_token = event.reply_token
        #push_template(id,buttons_template)
        send_template(reply_token, buttons_template)

    def on_enter_voteorange(self, event):
        user_id = event.source.user_id
        print(user_id)
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
                title='宋北北',
                text='你要投給宋楚瑜嗎?',
                thumbnail_image_url='https://i.imgur.com/vpxlYRd.jpg',
                actions=[
                    MessageTemplateAction(
                        label='好',
                        text='好'
                    ),
                    MessageTemplateAction(
                        label='不好',
                        text='不好'
                    ),
                ]
            )
        )
        reply_token = event.reply_token
        #push_template(id,buttons_template)
        send_template(reply_token, buttons_template)

    def on_enter_orangethank(self, event):
        user_id = event.source.user_id
        print(user_id)
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
                title='Thank you',
                text='宋伯伯感謝你',
                thumbnail_image_url='https://i.imgur.com/vpxlYRd.jpg',
                actions=[
                    MessageTemplateAction(
                        label='回到一開始',
                        text='回到一開始'
                    ),
                ]
            )
        )
        reply_token = event.reply_token
        #push_template(id,buttons_template)
        send_template(reply_token, buttons_template)


    def on_enter_u87(self, event):
        user_id = event.source.user_id
        print(user_id)
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
                title='Thank you',
                text='ㄍㄋㄋ你腦袋有問題嗎?????',
                thumbnail_image_url='https://i.imgur.com/guiku5e.jpg',
                actions=[
                    MessageTemplateAction(
                        label='回去重投',
                        text='好'
                    ),
                ]
            )
        )
        reply_token = event.reply_token
        #push_template(id,buttons_template)
        send_template(reply_token, buttons_template)



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