import math

from kivy.uix.screenmanager import Screen


class InductorCalculateTurns(Screen):

    def inductor_calculate_turns(self, henrys, diameter, oneturn):
        try:
            henrys = float(henrys)
            diameter = float(diameter) / 10                                 # в формуле сантиметры, во вводе миллиметры
            oneturn = float(oneturn) / 10
            inductor_length = (50 * oneturn ** 2 * henrys + math.sqrt(5) * math.sqrt(500 * oneturn ** 4 * henrys ** 2 +
                               9 * oneturn ** 2 * diameter ** 3 * henrys)) / diameter ** 2

            inductor_turns = inductor_length / oneturn
            inductor_turns_int = round(inductor_turns, 0)
            inductor_length_int = inductor_turns_int * oneturn * 10

            self.ids.inductor_length.text = "{:g} мм".format(inductor_length * 10)
            self.ids.inductor_length_int.text = "{:g} мм".format(inductor_length_int)
            self.ids.inductor_turns.text = "{:g} витка(ов)".format(inductor_turns)
            self.ids.inductor_turns_int.text = "{:g} витка(ов)".format(inductor_turns_int)
        except Exception:
            self.ids.inductor_length.text = "Неверный ввод!"
            self.ids.inductor_length_int.text = "Неверный ввод!"
            self.ids.inductor_turns.text = "Неверный ввод!"
            self.ids.inductor_turns_int.text = "Неверный ввод!"