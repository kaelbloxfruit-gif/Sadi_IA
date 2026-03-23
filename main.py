import socket
import requests
from collections import deque
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock

class ChatBot(BoxLayout):
    def __init__(self, **kwargs):
        super(ChatBot, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.chat_history = deque(maxlen=10)
        self.label = Label(size_hint_y=None, height=40)
        self.add_widget(self.label)
        self.text_input = TextInput(size_hint_y=None, height=40)
        self.add_widget(self.text_input)
        self.send_button = Button(text='Send', size_hint_y=None, height=40)
        self.send_button.bind(on_release=self.send_message)
        self.add_widget(self.send_button)

    def send_message(self, instance):
        user_input = self.text_input.text
        self.chat_history.append('You: ' + user_input)
        self.label.text = '\n'.join(self.chat_history)
        response = self.hablar_con_ia(user_input)
        self.chat_history.append('AI: ' + response)
        self.label.text = '\n'.join(self.chat_history)
        self.text_input.text = ''

    def rastrear_ip(self):
        try:
            response = requests.get('https://api.ipify.org?format=json')
            ip_info = response.json()
            return ip_info['ip']
        except requests.RequestException:
            return 'Could not retrieve IP.'

    def hablar_con_ia(self, user_input):
        # Dummy response, replace with actual logic
        return f'You said: {user_input}'

class ChatBotApp(App):
    def build(self):
        return ChatBot()

if __name__ == '__main__':
    ChatBotApp().run()