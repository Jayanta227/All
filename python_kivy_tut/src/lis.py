from kivy.app import App
from kivy.uix.listview import ListItemButton
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
Builder.load_string('''

#:import ListAdapter kivy.adapters.listadapter.ListAdapter
#:import ListItemButton kivy.uix.listview.ListItemButton
<RootWid>:
    orientation:'vertical'
    BoxLayout:
        size_hint_y:.2

        ListView:
            adapter:
                ListAdapter(data=['hello','hi','hello','hi','hello','hi','hello','hi'],cls=ListItemButton)
    BoxLayout:

''')



class RootWid(BoxLayout):
    pass
class RootApp(App):
    def build(self):
        return RootWid()


RootApp().run()