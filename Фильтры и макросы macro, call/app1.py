from jinja2 import Template

cars = [
    {'model': 'Ауди', 'price': 23000},
    {'model': 'Шкода', 'price': 17300},
    {'model': 'Вольво', 'price': 44300},
    {'model': 'Фольксваген', 'price': 21300}
]

l = [1, 2, 3, 4, 5]
tpl = "Суммарная цена {{ cars | sum(attribute='price')}}"  # Суммарная цена 105900
tpl = 'Сумма чисел от 1 до 5: {{ l | sum()}}'  # Сумма чисел от 1 до 5: 15
tpl = 'Максимальное число: {{ l | max(  ) }}'
tpl = 'Максимальная цена: {{ (cars | max(attribute="price")).model }}'
tpl = '{{ l | random }}'
tpl = '{{ cars | replace("о", "!") }}'

tm = Template(tpl)
print(tm.render(cars=cars, l=l))
