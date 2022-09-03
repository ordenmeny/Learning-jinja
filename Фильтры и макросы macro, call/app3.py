from jinja2 import Template

html = """
{%- macro input(name, value='', type='text', size=20) -%}
    <a type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}"></a>
{%- endmacro -%}
<p>{{ input(name='username') }}</p>
<p>{{ input(name='email', value='@gmail.com') }}</p>
<p>{{ input('password') }}</p>
"""
tm = Template(html)
msg = tm.render()

print(msg)