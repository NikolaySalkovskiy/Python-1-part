import random


class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self):
        a = random.randint(1, 2)
        if a == 1:
            print('Машина повернула налево')
        else:
            print('Машина повернула направо')

    def show_speed(self):
        print(f'Ваша скорость {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Вы превышаете скорость!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Вы превышаете скорость!')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


#Пример рабочей машины
my_work_car = WorkCar(100, "red", "Suzuki")
print(my_work_car.speed)
my_work_car.go()
my_work_car.turn()
my_work_car.show_speed()

#Пример спортивной машины
my_sport_car = SportCar(200, 'blue', 'Ferrari')
print(my_sport_car.speed)
print(my_sport_car.name)
my_sport_car.show_speed()
print(my_sport_car.is_police)

my_police_car = PoliceCar(100, 'blue', 'Mazda')
print(my_police_car.is_police)

my_town_car = TownCar(50, 'white', 'Hyundai')
my_town_car.show_speed()
