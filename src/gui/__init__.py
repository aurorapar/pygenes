import kivy
kivy.require('2.3.1')

from kivy.app import App
from kivy.core.window import Window

from translations import Translator, TRANSLATION
translator = Translator()

from gui.main_layout import MainLayout

Window.minimum_width = 800
Window.minimum_height = 600


class MainGui(App):

    def build(self):
        self.title = translator.translations[TRANSLATION.TITLE]
        self.root = root = MainLayout(anchor_x='right', anchor_y='top')
        return root
