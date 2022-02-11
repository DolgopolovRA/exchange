import random


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self):
        print(f'{self.name} повернула {random.choice(("налево", "направо"))}')

    def show_speed(self):
        print(f'Скорость {self.name} {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = False

    def show_speed(self):
        print(f'Скорость {self.name} {self.speed} км/ч')
        if self.speed > 60:
            print('Скорость превышает 60 км/ч!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = False


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = False

    def show_speed(self):
        print(f'Скорость {self.name} {self.speed} км/ч')
        if self.speed > 40:
            print('Скорость превышает 40 км/ч!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = True


town_car = TownCar(75, 'красный', 'Lada', False)
town_car.go()
town_car.turn()
town_car.show_speed()
town_car.stop()
work_car = WorkCar(55, 'белый', 'Газель', False)
work_car.go()
work_car.turn()
work_car.show_speed()
