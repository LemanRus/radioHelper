import os
# todo: MDScreenTitle для окон
from kivy.properties import ObjectProperty, StringProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IRightBodyTouch, OneLineListItem

import ResistorsMarking, CapacitorsMarking, ResistorLEDCalculateScreen, InductorCalculateTurns, \
    ParallelResistorCalculateScreen, SerialCapacitorCalculateScreen, VoltageDividerCalculateScreen, LM317Voltage, \
    LM317Current, InductorCalculateHenrys

from kivy.lang import Builder
from kivy.uix.spinner import SpinnerOption
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window


class CenterList(OneLineListItem):
    center_text = StringProperty()
    pass


class CenterItem(IRightBodyTouch, MDBoxLayout):
    text = StringProperty()
    pass


class NominalsScreen(MDScreen):
    pass


class Markings(MDScreen):
    pass


class Calculations(MDScreen):
    pass


class LM317CalculateScreen(MDScreen):
    pass


class InductorCalculateScreen(MDScreen):
    pass


class CalculationListScreen(MDScreen):
    pass


class Handbook(MDScreen):
    pass


class HandbookScreen(MDScreen):
    pass


class Pinout(MDScreen):
    pass


class AboutScreen(MDScreen):
    pass


class MySpinnerOption(SpinnerOption):
    colors = {"gold": [1, 0.84, 0, 1], "silver": [0.75, 0.75, 0.75, 1], "black": [0, 0, 0, 1],
              "brown": [0.4, 0.22, 0, 1], "red": [1, 0, 0, 1], "orange": [0.98, 0.45, 0.02, 1],
              "yellow": [1, 1, 0, 1], "green": [0.05, 0.64, 0.05, 1], "blue": [0.05, 0.54, 0.95, 1],
              "violet": [0.54, 0.14, 0.59, 1], "grey": [0.5, 0.5, 0.5, 1], "white": [1, 1, 1, 1]}


class RadioHelperMD(MDApp):

    screen_manager_for_back = ObjectProperty({})

    def add_me_to_sm(self, me, root_name):
        self.screen_manager_for_back[str(root_name)] = me

    def build(self):
        Window.bind(on_keyboard=self.Android_back_click)
        Builder.load_file("kv/misc.kv")
        kv = os.listdir("kv")
        for kv_file in kv:
            if kv_file != "misc.kv":
                Builder.load_file("kv/" + kv_file)
        return Builder.load_file("kv/main.kv")

    def Android_back_click(self, window, key, *largs):
        if key == 27:
            for key, value in self.screen_manager_for_back.items():
                if key == "calculations_sm":
                    if value.current in ["LM317_voltage", "LM317_current"]:
                        value.current = "lm317_cal"
                    elif value.current in ["inductor_turns", "inductor_henrys"]:
                        value.current = "inductor_cal"
                    else:
                        value.current = "calculations"
                if key == "markings_sm":
                    value.current = "nominals"
                if key == "handbook_sm":
                    value.current = "handbook"
            return True

RadioHelperMD().run()
