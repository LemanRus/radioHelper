import os
from kivy.properties import ObjectProperty, StringProperty
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.list import IRightBodyTouch, OneLineListItem
from StandardRows import StandardRows

import ResistorsMarking, CapacitorsMarking, ResistorLEDCalculateScreen, InductorCalculateTurns, \
    ParallelResistorCalculateScreen, SerialCapacitorCalculateScreen, LM317Voltage, \
    LM317Current, InductorCalculateHenrys

from kivy.lang import Builder
from kivy.uix.spinner import SpinnerOption
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window


class CenterList(OneLineListItem):
    center_text = StringProperty()
    pass


class CenterItem(IRightBodyTouch, MDBoxLayout):
    text = StringProperty()
    pass


class MD3Card(MDCard, RoundedRectangularElevationBehavior):
    """Implements a material design v3 card."""

    text = StringProperty()


class NominalsScreen(MDScreen):
    pass


class Markings(MDScreen):
    pass


class Calculations(MDScreen):
    pass


class LM317CalculateScreen(MDScreen):
    pass


class VoltageDividerCalculateScreen(MDScreen):
    pass


class VoltageDividerVout(MDScreen):
    def divider_calculate_vout(self, vin, r1, r2):
        try:
            vin = float(vin)
            r1 = float(r1)
            r2 = float(r2)

            vout = r2 * vin / (r1 + r2)
            rate = vin / vout

            self.ids.v_out.text = "{:g}".format(vout)
            self.ids.divider_rate.text = "{:g}".format(rate)
        except Exception:
            self.ids.v_out.text = "Неверный ввод!"
            self.ids.divider_rate.text = ""


class VoltageDividerR2(MDScreen):
    def divider_calculate_r(self, vin, vout, r1):
        try:
            vin = float(vin)
            vout = float(vout)
            r1 = float(r1)

            if vin <= vout:
                self.ids.r2_calculated.text = "Проверьте напряжения!"
                self.ids.divider_rate_r.text = ""
            else:
                r2 = r1 * vout / (vin - vout)
                rate = vin / vout

                self.ids.r2_calculated.text = "{:g}".format(r2)
                if r2 == 0:
                    self.ids.r2_calculated.text = "0 Ом (перемычка)"
                elif r2 < 1000:
                    self.ids.r2_calculated.text = "{:g} Ом".format(r2)
                elif r2 < 1000000:
                    self.ids.r2_calculated.text = "{:g} кОм".format(r2 / 1000)
                else:
                    self.ids.r2_calculated.text = "{:g} МОм".format(r2 / 1000000)

                self.ids.divider_rate_r.text = "{:g}".format(rate)

                e6_result = StandardRows.calculate_standard_resistor(r2, False)
                if e6_result == 0:
                    self.ids.r2_e24.text = "0 Ом (перемычка)"
                elif e6_result < 1000:
                    self.ids.r2_e24.text = "{:g} Ом".format(e6_result)
                elif e6_result < 1000000:
                    self.ids.r2_e24.text = "{:g} кОм".format(e6_result / 1000)
                else:
                    self.ids.r2_e24.text = "{:g} МОм".format(e6_result / 1000000)

                vout_corrected = e6_result * vin / (r1 + e6_result)
                self.ids.vout_e24.text = "{:g} В".format(vout_corrected)
        except (ZeroDivisionError, ValueError):
            self.ids.r2_calculated.text = "Неверный ввод!"
            self.ids.divider_rate_r.text = ""


class InductorCalculateScreen(MDScreen):
    pass


class CalculationListScreen(MDScreen):
    pass


class Handbook(MDScreen):
    pass


class HandbookScreen(MDScreen):
    pass


class Pinout(MDScreen):
    pass


class AboutScreen(MDScreen):
    pass


class MySpinnerOption(SpinnerOption):
    colors = {"Золотой": [1, 0.84, 0, 1], "Серебристый": [0.75, 0.75, 0.75, 1], "Чёрный": [0, 0, 0, 1],
              "Коричневый": [0.4, 0.22, 0, 1], "Красный": [1, 0, 0, 1], "Оранжевый": [0.98, 0.45, 0.02, 1],
              "Жёлтый": [1, 1, 0, 1], "Зелёный": [0.05, 0.64, 0.05, 1], "Синий": [0.05, 0.54, 0.95, 1],
              "Фиолетовый": [0.54, 0.14, 0.59, 1], "Серый": [0.5, 0.5, 0.5, 1], "Белый": [1, 1, 1, 1]}


class RadioHelperMD(MDApp):

    screen_manager_for_back = ObjectProperty({})

    def add_me_to_sm(self, me, root_name):
        self.screen_manager_for_back[str(root_name)] = me

    def build(self):
        Window.bind(on_keyboard=self.Android_back_click)
        Window.softinput_mode = 'below_target'
        Builder.load_file("kv/misc.kv")
        kv = os.listdir("kv")
        for kv_file in kv:
            if kv_file != "misc.kv":
                Builder.load_file("kv/" + kv_file)
        return Builder.load_file("kv/main.kv")

    def Android_back_click(self, window, key, *largs):
        if key == 27:
            for key, value in self.screen_manager_for_back.items():
                if key == "calculations_sm":
                    if value.current in ["LM317_voltage", "LM317_current"]:
                        value.current = "lm317_cal"
                    elif value.current in ["inductor_turns", "inductor_henrys"]:
                        value.current = "inductor_cal"
                    elif value.current in ["divider_vout", "divider_r2"]:
                        value.current = "divider_cal"
                    else:
                        value.current = "calculations"
                if key == "markings_sm":
                    value.current = "nominals"
                if key == "handbook_sm":
                    value.current = "handbook"
            return True

RadioHelperMD().run()
