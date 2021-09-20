from kivymd.app import MDApp

import ResistorScreen, CapacitorScreen, VoltageDividerCalculateScreen, ResistorLEDCalculateScreen, \
    InductorCalculateScreen, LM317Current, LM317Voltage, ParallelResistorCalculateScreen, \
    SerialCapacitorCalculateScreen, AboutScreen

import os
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.settings import SettingsWithSidebar
from kivy.config import Config
from kivy.uix.spinner import SpinnerOption

from settingsjson import settings_json

Config.read("radiohelper.ini")

kv = os.listdir("kv")
for kv_file in kv:
    Builder.load_file("kv/" + kv_file)


class RadioHelperScreenManager(ScreenManager):
    pass


class MainScreen(Screen):
    pass


class NominalsScreen(Screen):
    pass


class ComponentsScreen(Screen):
    pass


class LM317CalculateScreen(Screen):
    pass


class PinsScreen(Screen):
    pass


class SchemesScreen(Screen):
    pass


class SymbolsScreen(Screen):
    pass


class StatesScreen(Screen):
    pass


class HelpScreen(Screen):
    pass


class MySpinnerOption(SpinnerOption):
    colors = {"gold": [1, 0.84, 0, 1], "silver": [0.75, 0.75, 0.75, 1], "black": [0, 0, 0, 1],
              "brown": [0.4, 0.22, 0, 1], "red": [1, 0, 0, 1], "orange": [0.98, 0.45, 0.02, 1],
              "yellow": [1, 1, 0, 1], "green": [0.05, 0.64, 0.05, 1], "blue": [0.05, 0.54, 0.95, 1],
              "violet": [0.54, 0.14, 0.59, 1], "grey": [0.5, 0.5, 0.5, 1], "white": [1, 1, 1, 1]}


class RadioHelperApp(MDApp):

    app_font_size = NumericProperty()
    app_header_size = NumericProperty()
    app_button_size = NumericProperty()

    def build(self):
        self.icon = "img/icon.png"
        self.settings_cls = SettingsWithSidebar
        self.config.items("font")
        self.app_font_size = self.config.getint("font", "text_size")
        self.app_header_size = self.config.getint("font", "header_size")
        self.app_button_size = self.config.getint("font", "button_size")
        self.use_kivy_settings = False
        self.theme_cls.theme_style = "Dark"
        return RadioHelperScreenManager()

    def build_config(self, config):
        config.setdefaults("font", {
            "header_size": 30,
            "text_size": 30,
            "button_size": 30
        })

    def build_settings(self, settings):
        settings.add_json_panel("Размеры текста",
                                self.config,
                                data=settings_json)

    def on_config_change(self, config, section, key, value):
        config.set(section=section, option=key, value=value)
        config.write()
        self.app_font_size = self.config.getint("font", "text_size")
        self.app_header_size = self.config.getint("font", "header_size")
        self.app_button_size = self.config.getint("font", "button_size")
        self.root.ids.resistor.build_resistor(self.root.ids.resistor.ids.main_spinner.text)


if __name__ == '__main__':
    RadioHelperApp().run()
