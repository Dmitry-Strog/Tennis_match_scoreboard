import os

from jinja2 import Environment, FileSystemLoader

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates'))

# Создаем окружение Jinja2 с загрузчиком шаблонов из абсолютного пути
env = Environment(loader=FileSystemLoader(template_dir))


def render_page(html_name, **kwargs):
    """
    Функция для рендеринга HTML-шаблона с переданными переменными.

    :param html_name: Имя HTML-шаблона.
    :param kwargs: Переменные, которые будут использоваться в шаблоне.
    :return: Отрендеренный HTML-код.
    """
    template = env.get_template(html_name)
    return template.render(**kwargs)


