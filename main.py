import os

import ResistorsMarking, CapacitorsMarking

from kivy.lang import Builder
from kivy.uix.spinner import SpinnerOption
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class NominalsScreen(MDScreen):
    pass


class Markings(MDScreen):
    pass


class Calculations(MDScreen):
    pass


class Handbook(MDScreen):
    pass

class AboutScreen(MDScreen):
    pass


class MySpinnerOption(SpinnerOption):
    colors = {"gold": [1, 0.84, 0, 1], "silver": [0.75, 0.75, 0.75, 1], "black": [0, 0, 0, 1],
              "brown": [0.4, 0.22, 0, 1], "red": [1, 0, 0, 1], "orange": [0.98, 0.45, 0.02, 1],
              "yellow": [1, 1, 0, 1], "green": [0.05, 0.64, 0.05, 1], "blue": [0.05, 0.54, 0.95, 1],
              "violet": [0.54, 0.14, 0.59, 1], "grey": [0.5, 0.5, 0.5, 1], "white": [1, 1, 1, 1]}


class RadioHelperMD(MDApp):
    def build(self):
        Builder.load_file("kv/misc.kv")
        kv = os.listdir("kv")
        for kv_file in kv:
            if kv_file != "misc.kv":
                Builder.load_file("kv/" + kv_file)
        return Builder.load_file("kv/main.kv")


RadioHelperMD().run()
