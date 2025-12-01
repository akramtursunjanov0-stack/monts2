class Car:

    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.fined = False

    def drive_to(self, destination):
        print(f"Car {self.model} driving to {destination}")

    def change_color(self, new_color):
        self.color = new_color
        print(f"Car {self.model} changed to {self.color}")

car_honda = Car(color = "red", model = "Honda")
car_subaru = Car(color = "blue", model = "Subaru")
print(car_honda)
print(car_honda.color, car_honda.model)
car_honda.color = "green"
print(car_honda.color, car_honda.model)
print(car_subaru)
print(car_subaru.color, car_subaru.model)
car_honda.fined = True
print(car_honda.fined)
car_honda.year = 2020
print(car_honda.year)
car_subaru.year = 1999
print(car_subaru.year)
car_subaru.drive_to("Bishkek")
car_honda.drive_to("Karakol")
car_honda.change_color("silver")
