from kivy.uix.label import Label
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView


Builder.load_string('''
<ScrollableLabel>:
    text:str('some are really long string'*10)
    font_size:50
    text_size:self.size
''')
class ScrollableLabel(Label):
    pass
runTouchApp(ScrollableLabel())