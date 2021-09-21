from kivy.factory import Factory
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem


class Markings(Screen):
    pass


class Calculations(Screen):
    pass


class AboutScreen(Screen):
    pass


class RadioHelperMD(MDApp):
    def build(self):
        Builder.load_file("kv/markings.kv")
        Builder.load_file("kv/calculations.kv")
        Builder.load_file("kv/about_screen.kv")
        return Builder.load_file("kv/main.kv")


RadioHelperMD().run()
