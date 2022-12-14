from datetime import date


class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def calculateAge(self, age):
        pass

    @classmethod
    def objectBirthYear(cls, name, year):
        return cls(name, date.today().year - year)


obj1 = MyClass.objectBirthYear("Daniel", 1995)
obj1.age
