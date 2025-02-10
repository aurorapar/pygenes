import json
import os

from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from plyer import filechooser

from constants import FILE_EXTENSION, USER_HOME
import state
from translations import Translator, TRANSLATION

translator = Translator()

class FileSaver(Popup):

    def __init__(self, **kwargs):
        super(FileSaver, self).__init__(**kwargs)
        self.current_data = state.FAMILY_LINE

        self.title = translator.translations[TRANSLATION.FILE_SAVE]
        self.size_hint = [None, None]
        self.size = [600, 500]

        file_chooser_layout = GridLayout(cols=1)
        file_chooser_layout.spacing = [50, 10]

        file_chooser = FileChooserIconView()
        file_chooser.bind(selection=self.confirm_callback)
        file_chooser.rootpath = USER_HOME
        file_chooser.size_hint = [None, None]
        file_chooser.size = [self.size[0] - 25, self.size[1] * (3/5)]
        file_chooser.filters = ['*' + FILE_EXTENSION]
        self.file_chooser = file_chooser

        file_name_label = Label(text=translator.translations[TRANSLATION.ENTER_FILE_NAME])
        file_name_label.size_hint = (None,None)
        file_name_label.size = [50,30]
        file_name_label.padding = [50, 0, 0, 0]

        file_name_input = TextInput(multiline=False)
        file_name_input.bind(on_text_validate=self.confirm_callback)
        file_name_input.size_hint = [None, None]
        file_name_input.size = [self.size[0] - 50, 30]
        self.text_input = file_name_input

        file_chooser_button_layout = GridLayout(cols=2)
        file_chooser_button_layout.spacing = [50, 5]
        file_chooser_buttons = [
            (translator.translations[TRANSLATION.FILE_SAVE], self.confirm_callback, 50),
            (translator.translations[TRANSLATION.CANCEL], self.cancel_callback, 50),
        ]

        for button_text, button_callback, button_width in file_chooser_buttons:
            new_button = Button(text=button_text)
            new_button.bind(on_press=button_callback)
            new_button.size_hint = [None, None]
            new_button.size = [button_width, 40]
            file_chooser_button_layout.add_widget(new_button)
        file_chooser_button_layout.padding = [200, 0, 0, 0]

        file_chooser_layout.add_widget(file_chooser)
        file_chooser_layout.add_widget(file_name_label)
        file_chooser_layout.add_widget(file_name_input)
        file_chooser_layout.add_widget(file_chooser_button_layout)

        self.content = file_chooser_layout

    def execute(self):
        if not self.current_data:
            raise RuntimeError(translator.translations[TRANSLATION.NO_SAVE_DATA])

        self.open()

    def confirm_callback(self, instance, value=None):
        if isinstance(instance, FileChooserIconView):
            self.text_input.text = self.file_chooser.selection[0]
            return

        path = os.path.join(self.file_chooser.path, self.text_input.text)
        self.save_file(path)
        self.dismiss()

    def cancel_callback(self, instance):
        self.dismiss()

    def save_file(self, path):
        if not path.endswith(FILE_EXTENSION):
            path = os.path.join(path, FILE_EXTENSION)
        if not self.current_data.path == path:
            if not self.confirm_overwrite():
                return
        self.current_data.path = path
        with open(self.current_data.path, 'w') as f:
            json.dump(self.current_data, f)

    def confirm_overwrite(self):
        return True
