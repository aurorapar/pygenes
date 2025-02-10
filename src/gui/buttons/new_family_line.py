from kivy.core.window import Window
from kivy.graphics import Rectangle, Color
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

import state
from data_structures import FamilyLine
from file_operations import FileSaver
from gui.theme import FOREGROUND_COLOR
from translations import Translator, TRANSLATION
translator = Translator()

class NewFamilyLineLayout(FloatLayout):

    LAYOUT_SIZE = [200, 30]
    
    def __init__(self, **kwargs):
        super(NewFamilyLineLayout, self).__init__(**kwargs)

        self.size_hint = (None, None)
        self.size = NewFamilyLineLayout.LAYOUT_SIZE
        with self.canvas.before:
            Color(*FOREGROUND_COLOR)
            self.rect = Rectangle(size=self.size)
            self.rect.pos = (20, Window.size[1] - (NewFamilyLineLayout.LAYOUT_SIZE[1] + 50))
            self.pos = self.rect.pos
        
        new_button = Button()
        new_button.background_normal = ''
        new_button.background_color = FOREGROUND_COLOR
        new_button.text = translator.translations[TRANSLATION.NEW_FAMILY_LINE]
        self.add_widget(new_button)
        new_button.pos = self.pos
        self.button = new_button

        new_button.bind(on_press=self._create_family_line)

    def reposition(self):
        self.rect.pos = (20, Window.size[1] - (NewFamilyLineLayout.LAYOUT_SIZE[1] + 50))
        self.button.pos = self.rect.pos

    def _create_family_line(self, instance):
        global FAMILY_LINE
        family_line = FamilyLine()
        state.FAMILY_LINE = family_line
        FileSaver().execute()