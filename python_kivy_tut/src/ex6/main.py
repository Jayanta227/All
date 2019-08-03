"""
    ex4 has a problem that if we want to respond to an event it can't
    because listview is label. So in this code the problem is solved by
    listadapter and listitembutton
    """

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton

class LocationButton(ListItemButton):
    pass

class WeatherRoot(BoxLayout):
    pass
class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    
    def search_location(self):
        
        self.found_location()
        
    def found_location(self):
        
        self.search_results.item_strings.append(self.search_input.text)
        cities=self.search_results.item_strings
        self.search_results.adapter.data.clear()
        self.search_results.adapter.data.extend(cities)
        #self.search_results._trigger_reset_populate()
class WeatherApp(App):
    pass
if __name__=="__main__":
    WeatherApp().run()