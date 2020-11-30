class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Рисование ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Рисование карандашом')


class Handle(Stationery):
    def draw(self):
        print("Рисование маркером")


my_pen = Pen("Ручка")
my_pen.draw()

my_handle = Handle("Маркер")
my_handle.draw()

my_pencil = Pencil("Карандаш")
my_pencil.draw()
