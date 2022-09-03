from pip import *

data = '''{% raw %}Модуль Jinja вместо
определения {{name} }
подставляет соответствующее значение{% endraw %}
'''

tm = Template(data)
msg = tm.render(name='NAME')

print(msg)  # ... определения {{name} } ...
