import kivy
kivy.require('2.3.1')

from kivy.app import App
from kivy.uix.label import Label

class ErrorGui(App):

    def set_error_message(self, message):
        self.error_message = message

    def build(self):
        return Label(text=self.error_message, halign="center", markup=True)

def show_error(error_title, error_message):
    error_gui = ErrorGui()
    error_gui.title = error_title
    error_gui.set_error_message(error_message)
    error_gui.run()

