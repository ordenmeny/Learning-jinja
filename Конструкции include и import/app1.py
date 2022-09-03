from jinja2 import Environment, FileSystemLoader, FunctionLoader

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('page.html')
msg = tm.render(domain='google.com', title='Jinja')

print(msg)
