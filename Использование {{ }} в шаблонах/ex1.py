from pip import *

name = 'Dmitriy'
age = 16

# {{ }} - выражение для вставки конструкций Python в шаблоне
tm = Template('Меня зовут {{ n.upper() }}. И мне {{ a*2 }} лет')
msg = tm.render(n=name, a=age)  # n = 'Dmitriy'
print(msg)
