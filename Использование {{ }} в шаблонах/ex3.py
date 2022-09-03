from pip import *


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def func():
    return 'hi'


person = Person('Dmitriy', '01.06.2006')
tm = Template('{{p.name}}, {{p.age}}. {{func()}}')
msg = tm.render(p=person, func=func)
print(msg)
