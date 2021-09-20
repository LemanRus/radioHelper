import webbrowser

from kivy.uix.screenmanager import Screen


class AboutScreen(Screen):
    def link_to_founding(self, link):
        webbrowser.open(link)
