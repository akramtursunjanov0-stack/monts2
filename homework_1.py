class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education




    def introduce(self):
        education_text = (
            "у меня есть высшее образование"
            if self.higher_education
            else "у меня нет высшего образования"
        )
        print(
            f"Меня зовут {self.name}, "
            f"я родился {self.birth_date}, "
            f"по профессии я {self.occupation}, "
            f"{education_text}."
        )


person1 = Person("Андрей", "12.03.1995", "инженер", True)
person2 = Person("Мария", "25.07.1998", "дизайнер", False)
person3 = Person("Иван", "01.01.1990", "повар", True)

print(person1.name, person1.birth_date, person1.occupation, person1.higher_education)
print(person2.name, person2.birth_date, person2.occupation, person2.higher_education)
print(person3.name, person3.birth_date, person3.occupation, person3.higher_education)


person1.introduce()
person2.introduce()
person3.introduce()

