class Animal:
    def init(self, name, age):
        self.__name = name      # приватный атрибут
        self.__age = age        # приватный атрибут


    def get_name(self):
        return self.__name


    def set_name(self, name):
        if isinstance(name, str) and name:
            self.__name = name
        else:
            print("Ошибка: имя должно быть строкой")


    def get_age(self):
        return self.__age


    def set_age(self, age):
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            print("Ошибка: возраст должен быть положительным числом")

    def make_sound(self):
        print("Животное издаёт звук")


class Dog(Animal):
    def make_sound(self):
        print("Собака говорит: Гав!")


class Cat(Animal):
    def make_sound(self):
        print("Кошка говорит: Мяу!")



dog = Dog("Бобик", 3)
cat = Cat("Мурка", 2)


dog.make_sound()
cat.make_sound()

print(dog.get_name(), "-", dog.get_age())
print(cat.get_name(), "-", cat.get_age())

dog.set_name("Шарик")
dog.set_age(5)

cat.set_name("Снежок")
cat.set_age(4)

print(dog.get_name(), "-", dog.get_age())
print(cat.get_name(), "-", cat.get_age())