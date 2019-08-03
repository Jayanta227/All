from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.graphics import Color
from kivy.clock import Clock
import random


class RootWidget(GridLayout):
    pass

class MainApp(App):

    def build(self):
        parent = GridLayout(cols=6)
        Colour=[0,0,0,0]
        self.create_button(parent,Colour,1,1)
        Clock.schedule_interval(lambda a:self.update(parent), 1)
        return parent

    def update(self,obj):
        print ("I am update function")
        obj.clear_widgets()
        print ("random value is ",random.random())
        for i in (1,2,3,4,5,6):
            for j in (1,2,3,4,5,6):
                c=[random.random(),random.random(),random.random(),random.random()]
                d=[i,j]
                self.create_button(obj,c,i,j)

    def create_button(self,obj,color,i,j):

        a=Button(background_color=color,text='Hello World %s%s'%(i,j))
        obj.add_widget(a)




if __name__ == '__main__':
    MainApp().run()

