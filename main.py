from modules.residence import Residence
from modules.student import Student
from modules.car import Car

if __name__ == '__main__':
    students = [
        Student("Анна", 20, 101),
        Student("Дмитрий", 19, 102),
        Student("Елена", 21, 103)
    ]

    cars = [
        Car("А123ВС77", "Toyota Camry", "Белый", 180),
        Car("В456АВ33", "Lada Granta", "Красный", 106),
        Car("С789МН99", "BMW X5", "Чёрный", 300)
    ]

    residences = [
        Residence("Москва", "Арбат", 10, 25),
        Residence("Санкт-Петербург", "Невский проспект", 50, 101),
        Residence("Казань", "Пушкина", 15, 7)
    ]

    print('\nСтуденты:\n')

    for student in students:
        print(student)
        print(student.gender)
        print()

    print('\nМашины:\n')

    for car in cars:
        print(car)
        print(car.transport_tax())
        print(car.utilization_fee())
        print()

    print('\nМеста жительства:\n')

    for residence in residences:
        print(residence)
        print()