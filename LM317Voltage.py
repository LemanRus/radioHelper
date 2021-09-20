from kivy.uix.screenmanager import Screen
from StandardRows import StandardRows


class LM317Voltage(Screen):

    def calculate_lm317_voltage(self, vout, r1, iout, vin):
        try:
            vout = float(vout)
            r1 = float(r1)
            iout = float(iout)
            vin = float(vin)
            if iout > 5:
                self.ids.lm317_r2_output.text = "Ток нагрузки должен быть меньше 5А!"
                self.ids.lm317_r2_corrected_output.text = "Ток нагрузки должен быть меньше 5А!"
                self.ids.lm317_r2_output.text = ""
                self.ids.lm317_vout_output.text = ""
                self.ids.lm317_recommend_output.text = ""
                self.ids.lm317_power_output.text = ""
            else:
                r2 = r1 * (vout / 1.25 - 1)
                result = StandardRows.format_output_resistor(r2)

                r2_corrected = StandardRows.calculate_standard_resistor(r2, False)

                power = (vin - vout) * iout

                vout_corrected = 1.25 * (1 + r2_corrected / r1)

                if iout > 3:
                    recommend = "LM338"
                elif iout > 1.5:
                    recommend = "LM350"
                else:
                    recommend = "LM317"
                result_corrected = StandardRows.format_output_resistor(r2_corrected)

                self.ids.lm317_r2_corrected_output.text = result_corrected
                self.ids.lm317_r2_output.text = result
                self.ids.lm317_vout_output.text = "{:g} В".format(vout_corrected)
                self.ids.lm317_recommend_output.text = recommend
                self.ids.lm317_power_output.text = "{:g} Вт".format(power)

        except Exception:
            self.ids.lm317_r2_output.text = "Неверный ввод!"
            self.ids.lm317_r2_corrected_output.text = "Неверный ввод!"
            self.ids.lm317_r2_output.text = "Неверный ввод!"
            self.ids.lm317_vout_output.text = "Неверный ввод!"
            self.ids.lm317_recommend_output.text = "Неверный ввод!"
            self.ids.lm317_power_output.text = "Неверный ввод!"
