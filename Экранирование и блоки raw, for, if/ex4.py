from jinja2 import Template

cities = [
    {'id': 1, 'city': 'Москва'},
    {'id': 5, 'city': 'Tвеpь'},
    {'id': 7, 'city': 'MинCK'},
    {'id': 8, 'city': 'Cмоленск'},
    {'id': 11, 'city': 'Kanyгa'}
]

# -% убрать перенос строки
# link = """<select name="cities">
# {% for c in cities -%}
# {% if c.id > 6 -%}
#     <option value="{{c['id']}}">{{c['city']}}</option>
# {% else -%}
# {{c.city}}
# {% endif -%}
# {% endfor -%}
# </select>
# """

ip = [1, 5, 7, 8, 11]

link = """
{%- for i in ip -%}
{% if i > 5 -%}
number: {{i}}
{% else -%}
{{i}} <= 5
{% endif -%}
{% endfor -%}
!
"""


tm = Template(link)
msg = tm.render(cities=cities, ip=ip)
print(msg)