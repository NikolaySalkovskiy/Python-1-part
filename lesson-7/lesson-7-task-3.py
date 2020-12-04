class Cell:

    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        if self.number > other.number:
            return self.number - other.number
        else:
            return 'Разность меньше или равна 0'

    def __mul__(self, other):
        return self.number * other.number

    def __truediv__(self, other):
        return round(self.number / other.number)

    def make_order(self, in_line):
        constant = self.number
        while self.number > in_line:

            # Переменная, которая будет сохранять новую строку

            new = '*' * in_line
            print(new)
            new = ''
            self.number -= in_line
        new = '*' * self.number
        print(new)
        self.number = constant


cell = Cell(12)
cell.make_order(5)
print(cell.number)
example = Cell (10)
print(cell - example)
print(cell / example)
print(cell + example)
print(cell * example)
