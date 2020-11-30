
class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


example = Position("Николай", "Сальковский", "Ген директор", {'wage': 100000, 'bonus': 60000})
print(example.get_full_name())
print(example.get_total_income())
