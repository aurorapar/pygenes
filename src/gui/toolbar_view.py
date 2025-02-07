from kivy.uix.actionbar import ActionView, ActionButton, ActionPrevious, ActionGroup

from gui.toolbar_buttons import FileToolbarButton

from translations import Translator, TRANSLATION
translator = Translator()

class ToolbarView(ActionView):

    BUTTON_SPACING = 5

    def __init__(self, **kwargs):
        super(ToolbarView, self).__init__(**kwargs)
        self.use_separator = True
        self.action_previous = ActionPrevious()

        action_group = ActionGroup()
        action_group.pos_hint = {'left': 1}
        all_buttons = [
            FileToolbarButton()
        ]
        for button_index, button in enumerate(all_buttons):
            action_group.add_widget(button)

        self.add_widget(action_group)


