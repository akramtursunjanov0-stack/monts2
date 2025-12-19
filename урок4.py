class Person:


    def __init__(self, name, birth_date,  ):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education




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



class Classmate(Person):
    def __init__(self,name,birth_date,occupation,higher_education ,group_name):
        super().__init__(name,birth_date,occupation,higher_education)
        self.clas = group_name


    def introduce(self):
        print( f"Меня зовут {self.name}, "
            f"я родился {self.birth_date}, "
            f" я работаю {self.occupation}, "
            f"образование{self.higher_education}."
            f"Класс {self.clas}")




class Friend(Person):
    def __init__(self,name,birth_date,occupation,higher_education,hobby):
        super().__init__(name,birth_date,occupation,higher_education)
        self.hobby=hobby

    def introduce(self):
        print(f"Меня зовут {self.name}, "
              f"я родился {self.birth_date}, "
              f"я работаю {self.occupation}, "
              f" образование {self.higher_education}."
              f"мой хобби я{self.hobby}")


person1 = Friend("Akram","02,06,2006","програмист",True,"рисование")
person2 = Friend("Алекс","11,07,2000","учитель",True,"читение")
person3 = Classmate("Азим", "07,02,2003", "продавец",False,"11 a")
person4 = Classmate("Артур","08,06,2007","строитель", False,"11 Б")

data =[person1,person2,person3,person4]

for i in data:
    i.introduce()


