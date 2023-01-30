from kivy.uix.screenmanager import Screen
from StandardRows import StandardRows
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu


class ResistorLEDCalculateScreen(Screen):
    diodes = {'3 мм зелёный': (2.3, 20), '3 мм красный': (1.9, 20), '3 мм жёлтый': (2.1, 20), '3 мм синий': (2.9, 20),
              '5 мм зелёный': (2.3, 20), '5 мм красный': (1.9, 20), '5 мм жёлтый': (2.1, 20), '5 мм синий': (3.6, 75),
              '5 мм белый': (3.6, 75), '10 мм синий': (3.2, 20), '10 мм белый': (3.2, 20), 'Cree MX-3': (3.7, 350)}

    def build_menu(self):
        # [{"center_text": "3",
        #   "viewclass": "CenterList",
        #   "on_release": lambda x="3": self.set_item(x),
        #   "height": dp(56), },
        #  {"center_text": "4",
        #   "viewclass": "CenterList",
        #   "on_release": lambda x="4": self.set_item(x),
        #   "height": dp(56), },
        #  {"center_text": "5",
        #   "viewclass": "CenterList",
        #   "on_release": lambda x="5": self.set_item(x),
        #   "height": dp(56), },
        #  {"center_text": "6",
        #   "viewclass": "CenterList",
        #   "on_release": lambda x="6": self.set_item(x),
        #   "height": dp(56), }, ]
        self.menu_items = []
        for i in range(len(self.diodes.keys())):
            self.menu_items.append({"center_text": list(self.diodes.keys())[i], "viewclass": "CenterList",
                               "on_release": lambda x=list(self.diodes.keys())[i]: self.set_item(x),
                               "height": dp(56)})
        self.menu = MDDropdownMenu(
            caller=self.ids.resistor_marking_menu,
            items=self.menu_items,
            width_mult=4,
        )

    def build_me(self):
        self.build_menu()

    def set_item(self, text_item):
        self.ids.resistor_marking_menu_name.text = text_item
        self.menu.dismiss()

    def led_calculate(self, vol, led_vol, led_cur, led_quant):
        try:
            led_resistance = (float(vol) - (float(led_vol) * float(led_quant))) / (float(led_cur) / 1000)
            if led_resistance < 0:
                self.ids.led_result.text = "Слишком малое напряжение источника питания!"
                self.ids.led_res_power.text = ''
                self.ids.led_cur.text = ''
                self.ids.led_e24.text = ''
            else:
                self.ids.led_result.text = StandardRows.format_output_resistor(led_resistance)
                e24_result = StandardRows.calculate_standard_resistor(led_resistance, True)
                self.ids.led_e24.text = StandardRows.format_output_resistor(e24_result)

                self.ids.led_res_power.text = "{:g} мВт".format((float(vol) - float(led_vol)) *
                                                                float(led_cur) * float(led_quant))
                self.ids.led_cur.text = "{:g} мА".format(float(led_cur) * float(led_quant))
        except ValueError:
            self.ids.led_e24.text = "Неверный ввод!"
            self.ids.led_result.text = "Неверный ввод!"
            self.ids.led_res_power.text = "Неверный ввод!"
            self.ids.led_cur.text = "Неверный ввод!"