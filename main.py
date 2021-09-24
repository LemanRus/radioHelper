import os

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class NominalsScreen(MDScreen):
    pass


class Markings(MDScreen):
    pass


class Calculations(MDScreen):
    pass


class AboutScreen(MDScreen):
    pass


class ResistorsMarking(MDScreen):
    pass


class RadioHelperMD(MDApp):
    def build(self):
        Builder.load_file("kv/misc.kv")
        kv = os.listdir("kv")
        for kv_file in kv:
            if kv_file != "misc.kv":
                Builder.load_file("kv/" + kv_file)
        return Builder.load_file("kv/main.kv")


RadioHelperMD().run()
