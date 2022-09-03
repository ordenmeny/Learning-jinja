from jinja2 import Template

cities = [
    {'id': 1, 'city': 'Москва'},
    {'id': 5, 'city': 'Tвеpь'},
    {'id': 7, 'city': 'MинCK'},
    {'id': 8, 'city': 'Cмоленск'},
    {'id': 11, 'city': 'Kanyгa'}
]

# -% убрать перенос строки
link = """<select name="cities">
{% for c in cities -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% endfor -%}
</select>
"""

tm = Template(link)
msg = tm.render(cities=cities)
print(msg)