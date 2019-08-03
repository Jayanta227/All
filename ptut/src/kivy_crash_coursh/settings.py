from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
Builder.load_string('''
<Bl>:
    Button:
        text:'open settings'
        font_size:50
        on_release:app.open_settings()
''')
class Bl(BoxLayout):
    pass
class SettingsApp(App):
    def build(self):
        return Bl()
    def build_settings(self, settings):
        settings.add_json_panel('name',self.config,data='[{"type":"title","title":"example"}]')
SettingsApp().run()