import os

from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

from translations import Translator, TRANSLATION
translator = Translator()

class HelpDropdown(DropDown):

    def __init__(self, **kwargs):
        super(HelpDropdown, self).__init__(**kwargs)

        open_button = Button()
        open_button.text = translator.translations[TRANSLATION.ABOUT]
        open_button.bind(on_release=self._open_button_listener)
        open_button.height = 22
        open_button.size_hint_y = None
        self.add_widget(open_button)

    def _open_button_listener(self, test):
        print(os.listdir(DATA_FILE_DIR))