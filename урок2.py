# родительский класс, суперкласс
class Car:
    # инициализатор(конструктор)
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.fined = False

    def drive_to(self, destination):
        print(f"Car {self.model} driving to {destination}")

    def change_color(self, new_color):
        self.color = new_color
        print(f"Car {self.model} changed to {self.color}")


# дочерний класс, подкласс
class Bus(Car):
    pass


class Truck(Car):
    def drive_to(self, destination):
        print(f"Truck {self.model} driving to {destination}")

    def test(self):
        print(f"Truck test: {self.model}")



car_honda = Car(color = "red", model = "Honda")
car_subaru = Car(color = "blue", model = "Subaru")
car_subaru.drive_to("Karakol")
truck_1 = Truck("red", "Mercedes")
truck_1.drive_to("Bishkek")
print("Truck 1:", truck_1.color, truck_1.model)
truck_1.test()








