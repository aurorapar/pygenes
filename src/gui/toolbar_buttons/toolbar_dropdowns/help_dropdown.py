import os

from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from translations import Translator, TRANSLATION
translator = Translator()

class HelpDropdown(DropDown):

    def __init__(self, **kwargs):
        super(HelpDropdown, self).__init__(**kwargs)
        about_button = Button()
        about_button.text = translator.translations[TRANSLATION.ABOUT]
        about_button.bind(on_release=self._about_button_listener)
        about_button.height = 22
        about_button.size_hint_y = None
        self.add_widget(about_button)

    def _about_button_listener(self, instance):
        print(instance)
        content = Label(text=translator.translations[TRANSLATION.ABOUT_SECTION], size=[200,200])
        popup = Popup(
            title=translator.translations[TRANSLATION.ABOUT],
            content=content,
            size_hint=[None,None],
            size=[400, 200]
        )
        popup.open()
        self.dismiss()
