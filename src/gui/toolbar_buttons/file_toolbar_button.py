from kivy.uix.actionbar import ActionButton

from gui.toolbar_buttons.toolbar_dropdowns import FileDropdown

class FileToolbarButton(ActionButton):

    def __init__(self, **kwargs):
        super(FileToolbarButton, self).__init__(**kwargs)
        self.text = f' File '

        file_dropdown = FileDropdown()
        self.bind(on_release=file_dropdown.open)
