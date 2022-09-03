from jinja2 import Environment, FileSystemLoader

persons = [
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Hиолай", "old": 28, "weight": 82.3},
    {"name": "Mвaн", "old": 33, "weight": 94.0}
]

file_loader = FileSystemLoader('templates')  # из какого подкаталога будем брать шаблоны
env = Environment(loader=file_loader)

tm = env.get_template('main.html')  # Temlate
msg = tm.render(users=persons)
print(msg)
