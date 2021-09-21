from kivy.factory import Factory
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem


class MainScreen(MDBottomNavigation):
    pass


class Nominals(MDBottomNavigationItem):
    pass


class RadioHelperMD(MDApp):
    def build(self):
        self.root = Builder.load_file("kv/main_screen.kv")
        Builder.load_file("kv/nominals.kv")


RadioHelperMD().run()
