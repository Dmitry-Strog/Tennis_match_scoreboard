from src.templates.config_jinja import render_page


class ExceptionHandler:
    @classmethod
    def request_get(cls, environ, start_response):
        error = environ.get('exception')
        status = "200 OK"
        headers = [('Content-type', 'text/html; charset=utf-8')]
        start_response(status, headers)
        context = {
            "error": error,
        }
        rendered_html = render_page("exception.html", context)
        return [rendered_html.encode('utf-8')]
