import kivy
kivy.require('2.3.1')

from kivy.app import App
from kivy.core.window import Window

from translations import Translator, TRANSLATION
translator = Translator()

from gui.main_layout import MainLayout

class MainGui(App):

    def build(self):
        self.title = translator.translations[TRANSLATION.TITLE]
        self.root = root = MainLayout(anchor_x='right', anchor_y='top')
        Window.minimum_width = 800
        Window.minimum_height = 600
        Window.size = [800,600]
        return root
