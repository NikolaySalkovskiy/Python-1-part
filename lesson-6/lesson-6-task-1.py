import time

class TrafficLight:
    def __init__(self):
        self.__color = "red"

    def running(self):
        print(self.__color)
        time.sleep(7)
        self.__color = "yellow"
        print(self.__color)
        time.sleep(2)
        self.__color = "green"
        print(self.__color)
        time.sleep(5)
        print('Конец')



example = TrafficLight()
example.running()
