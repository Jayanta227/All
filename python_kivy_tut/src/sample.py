from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class TutorialsApp(App):
    def build(self):
        b=BoxLayout(orientation='vertical')
        t=TextInput(font_size=100,
                    height=200,
                    text="default")
        f=FloatLayout()
        s=Scatter()
        l=Label(text="Hello_Jayanta",
                font_size=150)
        #t.bind(text=l.setter("text"))
        f.add_widget(s)
        s.add_widget(l)
        
        b.add_widget(t)
        b.add_widget(f)
        return b

if __name__=="__main__":
    TutorialsApp().run()
