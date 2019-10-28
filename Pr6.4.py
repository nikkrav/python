"""
Опишите несколько классов: TownCar, SportCar, WorkCar, PoliceCar. У каждого класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также несколько методов: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
"""

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)
    def go(self):
        if self.speed != 0:
            print("Машина {} начала движение".format(self.name))

    def stop(self):
        if self.speed == 0:
            print("Машина {} остановилась".format(self.name))
    def direction(self, direction):
            print("Машина {} повернула {}".format(self.name, direction))



TownCar = Car(0, "white", "x", 0)
TownCar.go()
TownCar.direction("направо")
TownCar.stop()
SportCar = Car(10, "Red", "y", 0)
SportCar.go()
SportCar.direction("налево")
SportCar.stop()
WorkCar = Car(5, "Green", "z", 0)
WorkCar.go()
WorkCar.direction("налево")
WorkCar.stop()
PoliceCar = Car(800, "Blue", "trash", 1)
PoliceCar.go()
PoliceCar.direction("напрво")
PoliceCar.stop()


