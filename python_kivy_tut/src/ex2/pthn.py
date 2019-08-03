from kivy.app import App
import random
from kivy.uix.boxlayout import BoxLayout
class window(BoxLayout):
    pass
class tutorial(App):
    def build(self):
        return window()
if __name__=="__main__":
    tutorial().run()