from kivy.uix.screenmanager import Screen

from StandardRows import StandardRows


class CapacitorScreen(Screen):

    decimal_point = {"μ": 1000000, "u": 1000000, "p": 1, "n": 1000, "мк": 1000000, "н": 1000, "п": 1}
    voltage = {"G": 4, "J": 7, "A": 10, "C": 16, "D": 20, "E": 25, "V": 35}
    smd_capacity = {"A": 1., "E": 1.5, "J": 2.2, "N": 3.3, "S": 4.7, "W": 6.8}

    def calculate_capacitor(self, value):
        capacity = ""
        if value.isdigit():
            if len(value) <= 2:
                capacity = int(value)
            else:
                capacity = int(value[-2::-1][::-1]) * 10 ** int(value[-1])
        elif "R" in value:
            capacity = float("{}.{}".format(value.split("R")[0], value.split("R")[1]))
        elif any(ext in value for ext in self.decimal_point.keys()):
            intersection = "".join([inter for inter in self.decimal_point.keys() if (inter in value)])
            capacity = float("{}.{}".format(value.split(intersection)[0], value.split(intersection)[1])) *\
                self.decimal_point[intersection]
        else:
            self.ids.capacity.text = "Неверный ввод"

        if capacity != "":
            self.ids.capacity.text = StandardRows.format_output_capacitor(capacity)

    def calculate_smd_capacitor(self, value):
        capacity = ""
        if len(value) == 3:
            values = list(value)
            if values[0] in self.voltage.keys():
                voltage = self.voltage[values[0]]
            if values[0] not in self.voltage.keys():
                self.ids.smd_capacity.text = "Неверный ввод"
            elif values[1] in self.smd_capacity.keys():
                capacity = self.smd_capacity[values[1]] * 10 ** int(values[2])
            else:
                self.ids.smd_capacity.text = "Неверный ввод"
        else:
            self.ids.smd_capacity.text = "Неверный ввод"

        if capacity != "":
            self.ids.smd_capacity.text = StandardRows.format_output_capacitor(capacity) + ", " + str(voltage) + " В"
