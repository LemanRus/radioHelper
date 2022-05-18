from kivy.properties import DictProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextFieldRect

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
            self.dynamic_vars["card{}".format(self.counter)] = MDCard(padding=(10, 10, 10, 10))
            self.dynamic_vars["box{}".format(self.counter)].add_widget(self.dynamic_vars["card{}".format(self.counter)])
            self.dynamic_vars["input{}".format(self.counter)] = MDTextFieldRect(multiline=False,
                                                                                halign="center",
                                                                                size_hint=(1, None),
                                                                                height="30dp",
                                                                                pos_hint={"left": 1, "center_y": .5})
            self.dynamic_vars["card{}".format(self.counter)].add_widget(self.dynamic_vars["input{}".format(self.counter)
                                                                                          ])
            self.dynamic_vars["card_picofarad{}".format(self.counter)] = MDCard(padding=(10, 10, 10, 10),
                                                                                size_hint=(0.3, 1),)
            self.dynamic_vars["box{}".format(self.counter)].add_widget(self.dynamic_vars["card_picofarad{}".format(self.counter)])
            self.dynamic_vars["picofarad{}".format(self.counter)] = MDLabel(text="пФ",
                                                                            halign="center")
            self.dynamic_vars["card_picofarad{}".format(self.counter)].add_widget(
                self.dynamic_vars["picofarad{}".format(self.counter)])
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