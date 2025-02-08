from kivy.uix.actionbar import ActionButton

from gui.toolbar_buttons.toolbar_dropdowns import FileDropdown

from translations import Translator, TRANSLATION
translator = Translator()

class FileToolbarButton(ActionButton):

    def __init__(self, **kwargs):
        super(FileToolbarButton, self).__init__(**kwargs)
        self.text = ' ' + translator.translations[TRANSLATION.FILE_MENU_BUTTON] + ' '

        file_dropdown = FileDropdown()
        self.bind(on_release=file_dropdown.open)
