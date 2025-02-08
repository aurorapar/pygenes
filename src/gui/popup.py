import kivy

from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label

class PopupGui(App):

    def set_message(self, message):
        self.message = message

    def build(self):
        self.root = root = PopupLayout(anchor_x='left', anchor_y='top')
        root.set_message(self.message)
        Window.minimum_width = 400
        Window.minimum_height = 400
        Window.size = [400,400]
        return root

class PopupLayout(AnchorLayout):

    COLOR = [.1, .1, .1, 1]

    def __init__(self, **kwargs):
        super(PopupLayout, self).__init__(**kwargs)

        with self.canvas.before:
            Color(*PopupLayout.COLOR)  # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=Window.size)

        self.bind(size=self._size_update_listener)

        popup_label = Label(halign="center", markup=True)
        self.add_widget(popup_label)
        self.popup_label = popup_label

    def _size_update_listener(self, instance, value):
        self.rect.size = value

    def set_message(self, message):
        self.popup_label.text = message


def show_popup(title, message):
    Window.minimum_width = 200
    Window.minimum_height = 200
    popup = PopupGui()
    popup.title = title
    popup.set_message(message)
    popup.run()
    Window.size = [200,200]

