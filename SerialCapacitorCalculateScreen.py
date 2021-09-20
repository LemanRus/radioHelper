from kivy.app import App
from kivy.properties import DictProperty
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from StandardRows import StandardRows


class SerialCapacitorCalculateScreen(Screen):
    dynamic_vars = DictProperty({})
    counter = 0

    def reset(self):
        self.ids.ser_cap_box.clear_widgets()
        self.dynamic_vars.clear()
        self.counter = 0
        for i in range(0, 2):
            self.add_capacitor()

    def add_capacitor(self):
        try:
            self.dynamic_vars["box{}".format(self.counter)] = BoxLayout()
            self.ids["ser_cap_box"].add_widget(self.dynamic_vars["box{}".format(self.counter)])
            self.dynamic_vars["input{}".format(self.counter)] = TextInput(font_size=App.get_running_app().app_font_size,
                                                                          multiline=False,
                                                                          halign="center")
            self.dynamic_vars["box{}".format(self.counter
                                             )].add_widget(self.dynamic_vars["input{}".format(self.counter)])
            self.dynamic_vars["picofarad{}".format(self.counter)] = Label(text="пФ",
                                                                          font_size=App.get_running_app().app_font_size,
                                                                          halign="center")
            self.dynamic_vars["box{}".format(self.counter
                                             )].add_widget(self.dynamic_vars["picofarad{}".format(self.counter)])
            self.counter += 1
        except Exception:
            print("Heresy!!")

    def ser_cap_calculate(self):
        res_list = []
        try:
            for ids, value in self.dynamic_vars.items():
                if ids.startswith("input"):
                    res_list.append(1 / float(value.text))
            resistance = 1 / (sum(res_list))
            self.ids.ser_cap_output.text = StandardRows.format_output_capacitor(resistance)
        except ValueError:
            self.ids.ser_cap_output.text = "Неверный ввод!"
        except ZeroDivisionError:
            self.ids.ser_cap_output.text = StandardRows.format_output_capacitor(0)
