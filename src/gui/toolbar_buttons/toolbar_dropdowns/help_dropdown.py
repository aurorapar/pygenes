from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from translations import Translator, TRANSLATION
translator = Translator()

class HelpDropdown(DropDown):

    COLOR = [.3, .3, .3, 1]

    def __init__(self, **kwargs):

        super(HelpDropdown, self).__init__(**kwargs)

        buttons_and_callbacks = [
            (translator.translations[TRANSLATION.ABOUT], self._about_listener)
        ]

        for button_text, callback in buttons_and_callbacks:
            button = Button()
            button.background_normal = ''
            button.background_color = HelpDropdown.COLOR
            button.text = button_text
            button.bind(on_release=callback)
            button.height = 30
            button.size_hint_y = None
            self.add_widget(button)

    def _about_listener(self, instance):
        content = Label(text=translator.translations[TRANSLATION.ABOUT_SECTION], size=[200,200])
        popup = Popup(
            title=translator.translations[TRANSLATION.ABOUT],
            content=content,
            size_hint=[None,None],
            size=[400, 200]
        )
        popup.open()
        self.dismiss()
