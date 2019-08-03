from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    
    def search_location(self):
        self.search_results.item_strings.append(self.search_input.text)
        
    def found_location(self, request, data):
        pass
        
class WeatherApp(App):
    pass
if __name__=="__main__":
    WeatherApp().run()