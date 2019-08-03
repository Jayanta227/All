"""
    Use of factory to show an widget
    """
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.factory import Factory
from kivy.uix.listview import ListItemButton


class LocationButton(ListItemButton):
    pass

class WeatherRoot(BoxLayout):
    def show_current_weather(self,location):
        self.clear_widgets()
        current_weather=Factory.CurrentWeather()
        current_weather.location=location
        self.add_widget(current_weather)

    def show_add_location_form(self):
        self.clear_widgets()
        self.add_widget(AddLocationForm())
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
