from kivy.uix.actionbar import ActionButton

from gui.toolbar_buttons.toolbar_dropdowns import HelpDropdown

class HelpToolbarButton(ActionButton):

    def __init__(self, **kwargs):
        super(HelpToolbarButton, self).__init__(**kwargs)
        self.text = f' Help '

        help_dropdown = HelpDropdown()
        self.bind(on_release=help_dropdown.open)
