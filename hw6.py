from blessed import Terminal
from homework_1 import Person

term = Terminal()

# создаем объекты Person
person1 = Person("Акрам", "2000-01-01", "программист", True)
person2 = Person("Алина", "1999-05-10", "дизайнер", False)

person1.introduce()
person2.introduce()

print()  # пустая строка

# список фруктов (7 штук)
fruits = [
    (term.red, "🍎 Яблоко"),
    (term.yellow, "🍌 Банан"),
    (term.green, "🍏 Груша"),
    (term.magenta, "🍇 Виноград"),
    (term.bright_red, "🍓 Клубника"),
    (term.cyan, "🍉 Арбуз"),
    (term.bright_yellow, "🍍 Ананас"),
]

print(term.bold("Фрукты:\n"))

for color, fruit in fruits:
    print(color(fruit))