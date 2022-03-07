from kivy import Config
from kivy.app import App
from kivy.metrics import dp
from kivy.properties import DictProperty
from kivy.uix.spinner import Spinner
from kivy.uix.widget import Widget
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen

from StandardRows import StandardRows


class ResistorsMarking(MDScreen):

    dynamic_vars = DictProperty({})

    nominal = {"Чёрный": 0, "Коричневый": 1, "Красный": 2, "Оранжевый": 3, "Жёлтый": 4, "Зелёный": 5,
               "Синий": 6, "Фиолетовый": 7, "Серый": 8, "Белый": 9}
    multiplier = {"Золотой": 0.1, "Серебристый": 0.01, "Чёрный": 1, "Коричневый": 10, "Красный": 100, "Оранжевый": 1000, "Жёлтый": 10000,
                  "Зелёный": 100000, "Синий": 1000000, "Фиолетовый": 10000000, "Серый": 100000000}
    tolerance = {"Золотой": "±5%", "Серебристый": "±10%", "Чёрный": "±0,005%", "Коричневый": "±1%", "Красный": "±2%", "Оранжевый": "±0,01%",
                 "Жёлтый": "±0,02%", "Зелёный": "±0,5%", "Синий": "±0,25%", "Фиолетовый": "±0,1%", "Серый": "±0,05%"}
    thermal = {"Золотой": "±500 ppm/°С", "Серебристый": "±1000 ppm/°С", "Коричневый": "±100 ppm/°С", "Красный": "±50 ppm/°С",
               "Оранжевый": "±15 ppm/°С", "Жёлтый": "±25 ppm/°С", "Синий": "±10 ppm/°С", "Фиолетовый": "±5 ppm/°С",
               "Белый": "±1 ppm/°С"}
    colors = {"Золотой": [1, 0.84, 0, 1], "Серебристый": [0.8, 0.8, 0.8, 1], "Чёрный": [0, 0, 0, 1],
              "Коричневый": [0.4, 0.22, 0, 1], "Красный": [1, 0, 0, 1], "Оранжевый": [0.98, 0.45, 0.02, 1],
              "Жёлтый": [1, 1, 0, 1], "Зелёный": [0.05, 0.64, 0.05, 1], "Синий": [0.05, 0.54, 0.95, 1],
              "Фиолетовый": [0.54, 0.14, 0.59, 1], "Серый": [0.5, 0.5, 0.5, 1], "Белый": [1, 1, 1, 1]}
    eia96 = {"01": 100, "02": 102, "03": 105, "04": 107, "05": 110, "06": 113, "07": 115, "08": 118, "09": 121,
             "10": 124, "11": 127, "12": 130, "13": 133, "14": 137, "15": 140, "16": 143, "17": 147, "18": 150,
             "19": 154, "20": 158, "21": 162, "22": 165, "23": 169, "24": 174, "25": 178, "26": 182, "27": 187,
             "28": 191, "29": 196, "30": 200, "31": 205, "32": 210, "33": 215, "34": 221, "35": 226, "36": 232,
             "37": 237, "38": 243, "39": 249, "40": 255, "41": 261, "42": 267, "43": 274, "44": 280, "45": 287,
             "46": 294, "47": 301, "48": 309, "49": 316, "50": 324, "51": 332, "52": 340, "53": 348, "54": 357,
             "55": 365, "56": 374, "57": 383, "58": 392, "59": 402, "60": 412, "61": 422, "62": 432, "63": 442,
             "64": 453, "65": 464, "66": 475, "67": 487, "68": 499, "69": 511, "70": 523, "71": 536, "72": 549,
             "73": 562, "74": 576, "75": 590, "76": 604, "77": 619, "78": 634, "79": 649, "80": 665, "81": 681,
             "82": 698, "83": 715, "84": 732, "85": 750, "86": 768, "87": 787, "88": 806, "89": 825, "90": 845,
             "91": 866, "92": 887, "93": 909, "94": 931, "95": 953, "96": 976}
    eia96_multiplier = {"Z": 0.001, "Y": 0.01, "R": 0.01, "X": 0.1, "S": 0.1, "A": 1, "B": 10, "H": 10, "C": 100,
                        "D": 1000, "E": 10000, "F": 100000}

    def build_menu(self):
        menu_items = [{"center_text": "3",
                       "viewclass": "CenterList",
                       "on_release": lambda x="3": self.set_item(x),
                       "height": dp(56),},
                      {"center_text": "4",
                       "viewclass": "CenterList",
                       "on_release": lambda x="4": self.set_item(x),
                       "height": dp(56),},
                      {"center_text": "5",
                       "viewclass": "CenterList",
                       "on_release": lambda x="5": self.set_item(x),
                       "height": dp(56),},
                      {"center_text": "6",
                       "viewclass": "CenterList",
                       "on_release": lambda x="6": self.set_item(x),
                       "height": dp(56),}, ]
        self.menu = MDDropdownMenu(
            caller=self.ids.resistor_marking_menu,
            items=menu_items,
            width_mult=4,
        )

    def set_item(self, text_item):
        self.ids.resistor_marking_menu_name.text = text_item
        self.menu.dismiss()
        self.build_resistor(self.ids.resistor_marking_menu_name.text)

    def build_me(self):
        self.build_menu()
        self.build_resistor(3)

    def calculate_resistor(self):

        thermal = ""
        tolerance = ""

        if "band5" in self.dynamic_vars.keys():
            thermal = self.thermal[self.dynamic_vars["band5"].text]
        if "band4" in self.dynamic_vars.keys():
            tolerance = self.tolerance[self.dynamic_vars["band4"].text]
        if len(self.ids["resistor_bands"].children) == 5 or len(self.ids["resistor_bands"].children) == 7:
            multiplier = self.multiplier[self.dynamic_vars["band2"].text]
            resistance = (self.nominal[self.dynamic_vars["band0"].text] * 10 +
                          self.nominal[self.dynamic_vars["band1"].text]) * multiplier

            if "band3" in self.dynamic_vars.keys():
                tolerance = self.tolerance[self.dynamic_vars["band3"].text]
            else:
                tolerance = "±20%"
        else:
            multiplier = self.multiplier[self.dynamic_vars["band3"].text]
            resistance = (self.nominal[self.dynamic_vars["band0"].text] * 100 +
                          self.nominal[self.dynamic_vars["band1"].text] * 10 +
                          self.nominal[self.dynamic_vars["band2"].text]) * multiplier

        if resistance < 1000:
            self.ids.resistance.text = "{:g} Ом {}{}".format(resistance, tolerance,
                                                             (", ТКС: " + thermal) if thermal else "")
        elif resistance < 1000000:
            self.ids.resistance.text = "{:g} кОм {}{}".format(resistance / 1000, tolerance,
                                                              (", ТКС: " + thermal) if thermal else "")
        else:
            self.ids.resistance.text = "{:g} МОм {}{}".format(resistance / 1000000, tolerance,
                                                              (", ТКС: " + thermal) if thermal else "")

    def build_resistor(self, value):
        bands = {3: {0: tuple(self.nominal.keys())[1:], 1: tuple(self.nominal.keys()), 2: tuple(self.multiplier.keys())},
                 4: {0: tuple(self.nominal.keys())[1:], 1: tuple(self.nominal.keys()), 2: tuple(self.multiplier.keys()),
                     3: tuple(self.tolerance.keys())},
                 5: {0: tuple(self.nominal.keys())[1:], 1: tuple(self.nominal.keys()), 2: tuple(self.nominal.keys()),
                     3: tuple(self.multiplier.keys()), 4: tuple(self.tolerance.keys())},
                 6: {0: tuple(self.nominal.keys())[1:], 1: tuple(self.nominal.keys()), 2: tuple(self.nominal.keys()),
                     3: tuple(self.multiplier.keys()), 4: tuple(self.tolerance.keys()), 5: tuple(self.thermal.keys())},
                 }

        self.ids.resistor_bands.clear_widgets()
        self.dynamic_vars.clear()

        for bands_qty in range(0, int(value)):
            try:
                self.dynamic_vars["band{}".format(bands_qty)] = Spinner(text=bands[int(value)][bands_qty][0],
                                                                        values=list(bands[int(value)][bands_qty]),
                                                                        background_color=self.colors[
                                                                            bands[int(value)][bands_qty][0]],
                                                                        color=[0, 0, 0, 0],  # if bands[
                                                                            #                       int(value)][
                                                                            #                       bands_qty][
                                                                            #                       0] == "Золотой" else [
                                                                            # 1, 1, 1, 1],
                                                                        background_normal="",
                                                                        option_cls="MySpinnerOption",)
                self.ids["resistor_bands"].add_widget(self.dynamic_vars["band{}".format(bands_qty)])
                for key, band in self.dynamic_vars.items():
                    if key.startswith("band"):
                        band.bind(text=self.colourize)
                if bands_qty < int(value) - 1:
                    self.dynamic_vars["gap{}".format(bands_qty)] = Widget(size_hint_x=0.4)
                    self.ids["resistor_bands"].add_widget(self.dynamic_vars["gap{}".format(bands_qty)])
            except KeyError:
                continue

    def colourize(self, *args):
        for key, band in self.dynamic_vars.items():
            if key.startswith("band"):
                band.background_color = self.colors[band.text]
                # if band.text == "Жёлтый" or band.text == "Золотой" or band.text == "Белый":
                #     band.color = [0, 0, 0, 1]
                # else:
                #     band.color = [1, 1, 1, 1]

    def calculate_smd_resistor(self, marking):
        try:
            self.ids.smd_resistance.text = ""
            resistance = ""
            if marking in ["0", "00", "000", "0000"]:
                resistance = 0
            elif "R" in marking and marking[2] != "R":
                if len(marking) == 3 or len(marking) == 4:
                    markings = marking.split("R")
                    resistance = float("{}.{}".format(markings[0], markings[1]))
                else:
                    self.ids.smd_resistance.text = "Неверный ввод"
            elif "r" in marking:
                if len(marking) == 3 or len(marking) == 4:
                    markings = marking.split("r")
                    resistance = float("{}.{}".format(markings[0], markings[1]))
                else:
                    self.ids.smd_resistance.text = "Неверный ввод"
            elif len(marking) == 3:
                if marking[2].isalpha() and marking[2] in self.eia96_multiplier.keys():
                    multiplier = self.eia96_multiplier[marking[2]]
                    resistance = self.eia96[marking[:2]] * multiplier
                else:
                    resistance = float(marking[:2]) * 10 ** (float(marking[2]))
            elif len(marking) == 4:
                resistance = float(marking[:3]) * 10 ** (float(marking[3]))
            else:
                self.ids.smd_resistance.text = "Неверный ввод"

            if resistance != "":
                self.ids.smd_resistance.text = StandardRows.format_output_resistor(resistance)
        except ValueError:
            self.ids.smd_resistance.text = "Неверный ввод!"
