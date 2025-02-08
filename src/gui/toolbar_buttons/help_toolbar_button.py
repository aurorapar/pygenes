from kivy.uix.actionbar import ActionButton

from gui.toolbar_buttons.toolbar_dropdowns import HelpDropdown

from translations import Translator, TRANSLATION
translator = Translator()

class HelpToolbarButton(ActionButton):

    def __init__(self, **kwargs):
        super(HelpToolbarButton, self).__init__(**kwargs)
        self.text = ' ' + translator.translations[TRANSLATION.HELP_MENU_BUTTON] + ' '

        help_dropdown = HelpDropdown()
        self.bind(on_release=help_dropdown.open)
