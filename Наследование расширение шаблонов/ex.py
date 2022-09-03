from jinja2 import Environment, FileSystemLoader

subs = ['Math', 'physics', 'Informatics', 'Russian language']
file_loader = FileSystemLoader('templates')  # шаблоны берём из каталога templates
env = Environment(loader=file_loader)

template = env.get_template('about.html')  # сам шаблон

output = template.render(list_table=subs)
print(output)
