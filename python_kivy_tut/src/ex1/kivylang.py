from kivy.uix.boxlayout import BoxLayout
import urllib.request, urllib.parse, urllib.error
from kivy.app import App
class bxlayout(BoxLayout):
    fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt').read()
    st=fhand.decode()
class kivylanguage(App):
    def build(self):
        return bxlayout()
if __name__=="__main__":
    kivylanguage().run()