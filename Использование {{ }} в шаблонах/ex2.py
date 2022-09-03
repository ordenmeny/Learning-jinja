from pip import *


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        self.__name = val

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, val):
        self.__age = val


per = Person('Dmitriy', 16)

tm = Template('Меня зовут {{ p.name }}. И мне {{ p.age }} лет')
msg = tm.render(p=per)
print(msg)
