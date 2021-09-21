from kivymd.app import MDApp
from kivymd.uix.bottomnavigation import MDBottomNavigation


class MainScreen(MDBottomNavigation):
    pass

class RadioHelperMD(MDApp):
    def build(self):
        return MainScreen()


RadioHelperMD().run()
