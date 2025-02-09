from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.actionbar import ActionBar

from gui.toolbar_view import ToolbarView


class ToolbarWidget(ActionBar):

    LAYOUT_SIZE = [Window.width, 25]
    COLOR = [.2, .2, .2]

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(ToolbarWidget, self).__init__(**kwargs)
        self.size_hint = [None,None]
        self.size = ToolbarWidget.LAYOUT_SIZE
        self.background_image = ''
        self.background_color = ToolbarWidget.COLOR
        self.bind(size=self._update_rect, pos=self._update_rect)

        self._add_action_view()

    def _update_rect(self, instance, value):
        ToolbarWidget.LAYOUT_SIZE[0] = Window.width
        self.pos = (0, Window.height - ToolbarWidget.LAYOUT_SIZE[1])
        self.size = ToolbarWidget.LAYOUT_SIZE
        self.toolbar.padding = [0, 0, Window.size[0] - 150, 0]

    def _add_action_view(self):
        toolbar = ToolbarView()
        self.add_widget(toolbar)
        self.toolbar = toolbar
        self.toolbar.padding = [0, 0, Window.size[0] - 150, 0]
