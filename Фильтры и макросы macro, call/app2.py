from jinja2 import Template

persons = [
    {"name": "Алексeй", "old": 18, "weight": 78.5},
    {"name": "николай", "old": 28, "weight": 82.3},
    {"name": "Ивaн", "old": 33, "weight": 94.0}
]

tpl = """
{%- for u in users -%}
{% filter upper %}{{ u.name }}{% endfilter %}
{% endfor -%}
"""
tpl = """
{%- for u in users -%}
{% filter lower %}{{ u.name }}{% endfilter %}
{% endfor -%}
"""

tp = Template(tpl)
msg = tp.render(users=persons)
print(msg)