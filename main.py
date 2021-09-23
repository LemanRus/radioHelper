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
        Builder.load_file("kv/markings.kv")
        Builder.load_file("kv/calculations.kv")
        Builder.load_file("kv/about_screen.kv")
        Builder.load_file("kv/nominals.kv")
        Builder.load_file("kv/resistors_marking.kv")
        return Builder.load_file("kv/main.kv")


RadioHelperMD().run()
