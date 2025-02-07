import kivy
kivy.require('2.3.1')

from kivy.app import App
from kivy.uix.widget import Widget

from translations import Translator, TRANSLATION
translator = Translator()

class MainWidget(Widget):
    pass

class MainGui(App):
    def build(self):
        self.title = translator.translations[TRANSLATION.TITLE]
        return MainWidget()
