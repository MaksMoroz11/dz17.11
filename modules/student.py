class Student:
    def __init__(self, name: str, age: int, group: int):
        self.name = name
        self.age = age
        self.group = group

    def __str__(self):
        return f'{self.name} {self.age} {self.group}'

    @property
    def gender(self):
        return 'ж' if self.name[-1] == 'а' else 'м'