from kivy.uix.actionbar import ActionView, ActionButton, ActionPrevious, ActionGroup

from gui.toolbar_buttons import FileToolbarButton, HelpToolbarButton

class ToolbarView(ActionView):

    def __init__(self, **kwargs):
        super(ToolbarView, self).__init__(**kwargs)
        self.use_separator = False
        self.action_previous = ActionPrevious()
        self.action_previous.app_icon = ''
        self.action_previous.app_icon_width = 0
        self.action_previous.app_icon_height = 0

        # action_group.pos_hint = {'left': 1}
        all_buttons = [
            FileToolbarButton(),
            HelpToolbarButton()
        ]

        for button in all_buttons:
            self.add_widget(button)
