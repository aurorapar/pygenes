import os

from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

from file_operations import DATA_FILE_DIR
from translations import Translator, TRANSLATION
translator = Translator()

class FileDropdown(DropDown):

    COLOR = [.3, .3, .3, 1]

    def __init__(self, **kwargs):
        super(FileDropdown, self).__init__(**kwargs)

        buttons_and_callbacks = [
            (translator.translations[TRANSLATION.FILE_NEW], self._new_listener),
            (translator.translations[TRANSLATION.FILE_OPEN], self._open_listener),
            (translator.translations[TRANSLATION.FILE_SAVE], self._save_listener),
            (translator.translations[TRANSLATION.FILE_CLOSE], self._close_listener),
        ]

        for button_text, callback in buttons_and_callbacks:
            button = Button()
            button.background_normal = ''
            button.background_color = FileDropdown.COLOR
            button.text = ' ' + button_text + ' '
            button.bind(on_release=callback)
            button.height = 30
            button.size_hint_y = None
            self.add_widget(button)

    def _new_listener(self, instance):
        self.dismiss()
        project_files = os.listdir(DATA_FILE_DIR)

    def _open_listener(self, instance):
        self.dismiss()

    def _save_listener(self, instance):
        self.dismiss()

    def _close_listener(self, instance):
        self.dismiss()


