class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, car_direction):
        print(f'Машина повернула {car_direction}')

    def show_speed(self):
        print(f'Скорость авто: {self.speed}')

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Превышение скорости')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Превышение скорости')

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

town = TownCar(90, 'green', 'Town')
sport = SportCar(120, 'red', 'Sport')
work = WorkCar(41, 'yellow', 'Work')
police = PoliceCar(100, 'blue', 'police')

town.show_speed()
work.show_speed()

work.speed = 30
work.show_speed()

police.turn('Left')