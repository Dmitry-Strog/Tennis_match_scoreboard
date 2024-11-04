from src.templates.config_jinja import render_page


class IndexHandler:
    @classmethod
    def request_get(cls, environ, start_response):
        status = "200 OK"
        headers = [('Content-type', 'text/html; charset=utf-8')]
        start_response(status, headers)
        rendered_html = render_page("index.html")
        return [rendered_html.encode('utf-8')]
