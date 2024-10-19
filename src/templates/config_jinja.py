import os

from jinja2 import Environment, FileSystemLoader

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates'))

# Создаем окружение Jinja2 с загрузчиком шаблонов из абсолютного пути
env = Environment(loader=FileSystemLoader(template_dir))


def render_page(html_name, context: dict = None):
    if context is None:
        context = {}
    template = env.get_template(html_name)
    return template.render(context)



