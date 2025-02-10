import os

from kivy.uix.actionbar import ActionView, ActionButton, ActionPrevious, ActionGroup
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from plyer import filechooser

from constants import FILE_EXTENSION, USER_HOME
from gui.theme import FOREGROUND_COLOR
from translations import Translator, TRANSLATION

translator = Translator()

class ToolbarView(ActionView):

    LAYOUT_HEIGHT = 25
    COLOR = FOREGROUND_COLOR

    def __init__(self, **kwargs):
        super(ToolbarView, self).__init__(**kwargs)

        self.use_separator = False
        self.action_previous = ActionPrevious()
        self.action_previous.app_icon = ''
        self.action_previous.app_icon_width = 0
        self.action_previous.app_icon_height = 0

        # action_group.pos_hint = {'left': 1}
        all_groups = {
            translator.translations[TRANSLATION.FILE_MENU_BUTTON]: [
                (translator.translations[TRANSLATION.FILE_NEW], self._new_listener),
                (translator.translations[TRANSLATION.FILE_OPEN], self._open_listener),
                (translator.translations[TRANSLATION.FILE_SAVE], self._save_listener),
                (translator.translations[TRANSLATION.FILE_CLOSE], self._close_listener),
            ],
            translator.translations[TRANSLATION.HELP_MENU_BUTTON]: [
                (translator.translations[TRANSLATION.ABOUT], self._about_listener)
            ]
        }

        for group_name, button_text_callback in all_groups.items():
            action_group = ActionGroup()
            action_group.text = group_name
            action_group.mode = 'spinner'
            for button_text, button_callback in button_text_callback:
                action_button = ActionButton()
                action_button.background_normal = ''
                action_button.background_image = ''
                action_button.background_color = ToolbarView.COLOR
                action_button.text = ' ' + button_text + ' '
                action_button.bind(on_release=button_callback)
                # action_button.height = 30
                # action_button.size_hint_y = None
                action_group.add_widget(action_button)
            self.add_widget(action_group)

    def _new_listener(self, instance):
        project_files = os.listdir()

    def _open_listener(self, instance):
        selection = filechooser.open_file(
            title=translator.translations[TRANSLATION.FILE_OPEN],
            filters = [("PyGene Files", f"*{FILE_EXTENSION}")],
            path=USER_HOME
        )
        print(selection)

    def _save_listener(self, instance):
        selection = filechooser.save_file(title=translator.translations[TRANSLATION.FILE_SAVE], path=USER_HOME)
        print(selection)

    def _close_listener(self, instance):
        pass

    def _about_listener(self, instance):
        content = Label(text=translator.translations[TRANSLATION.ABOUT_SECTION], size=[200, 200])
        popup = Popup(
            title=translator.translations[TRANSLATION.ABOUT],
            content=content,
            size_hint=[None, None],
            size=[400, 200]
        )
        popup.open()

