from jinja2 import Environment, FileSystemLoader, FunctionLoader

persons = [
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Hиолай", "old": 28, "weight": 82.3},
    {"name": "Mвaн", "old": 33, "weight": 94.0}
]


def loadTpl(path):
    if path == 'index':
        return """Имя: {{ u.name }}, возраст: {{ u.old }}"""

    else:
        return """Данные: {{ u }}"""


file_loader = FunctionLoader(loadTpl)
env = Environment(loader=file_loader)

tm = env.get_template('index')  # Temlate
msg = tm.render(u=persons[0])
print(msg)
