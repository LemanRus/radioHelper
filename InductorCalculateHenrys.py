import math

from kivy.uix.screenmanager import Screen


class InductorCalculateHenrys(Screen):

    def inductor_calculate_henrys(self, turns, diameter, length):
        try:

            turns = float(turns)
            diameter = float(diameter)
            length = float(length)

            formfactor = length / diameter

            induction = 0.0002 * math.pi * diameter * turns ** 2 * (math.log(1 + math.pi/(2 * formfactor)) +
                                                                    1 / (2.3004 + 3.437 * formfactor + 1.7636 *
                                                                         formfactor ** 2 - 0.47 / (0.755 + 1 /
                                                                                                   formfactor) ** 1.44))
            self.ids.induction.text = "{:g} мкГн".format(induction)
        except Exception:
            self.ids.induction.text = "Неверный ввод!"