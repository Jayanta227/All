from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


Builder.load_string('''
<Root1>:
    orientation:'vertical'
    canvas:
        Color:
            rgba:.5, .4, 1,.2
        Rectangle:
            pos:self.pos
            size:self.size
    Button:
        text:'click'
        size_hint_y:.2
        on_press:root.ch_pos1
    Widget:
        Round:
            id:rd
<Round>:
    pos_hint:None,None
    pos:300,200
    size:100,100
    canvas:
        Color:
            rgba:0,1,1,1
        Ellipse:
            pos:self.pos
            size:self.size
    
                
''')
class Root1(BoxLayout):
    def ch_pos1(self):
        Round().ch_pos2()
class Round(Widget):
    def ch_pos2(self):
        self.center_x=100
runTouchApp(Root1())