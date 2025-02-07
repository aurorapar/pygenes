import os

from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

from file_operations import DATA_FILE_DIR
from translations import Translator, TRANSLATION
translator = Translator()

class FileDropdown(DropDown):

    def __init__(self, **kwargs):
        super(FileDropdown, self).__init__(**kwargs)

        open_button = Button()
        open_button.text = translator.translations[TRANSLATION.FILE_OPEN]
        open_button.bind(on_release=self._open_button_listener)
        open_button.height = 22
        open_button.size_hint_y = None
        self.add_widget(open_button)

    def _open_button_listener(self, test):
        print(os.listdir(DATA_FILE_DIR))