from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.clock import Clock


class RootWid(BoxLayout):
    px=0
    py=0
    def move(self):
        self.ref.canvas.clear()
        with self.ref.canvas:
            Color(0,1,1,.8)
            Rectangle(pos=(50,50),size=(100,100))
    def update(self):
        Clock.schedule_interval(self.update1, 1/60.)
    def update1(self,*args):
        self.ref.canvas.clear()
        
        self.px=self.px+10
        self.py=self.py+3
        
        with self.ref.canvas:
            Color(0,1,1,.8)
            Rectangle(pos=(self.px,self.py),size=(50,50))
class CircleApp(App):
    def build(self):
        return RootWid()
if __name__=="__main__":
    CircleApp().run()