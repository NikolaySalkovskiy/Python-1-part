class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def count_weight(self):
        return self._length * self._width * 25 * 5


my_road = Road(15000, 50)
print(my_road.count_weight())
