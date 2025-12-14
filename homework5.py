class Vehicle():
    def start(self):
        print("Vehecle starting")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car starting")


class ElectricCar():
    def start(self):
        super().start()



class Tesla (ElectricCar, Car):
    def start(self):
        super().start()
        print("Tesla ready")


das = Tesla()
das.start()