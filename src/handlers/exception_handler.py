from src.exceptions import NotFoundError, DuplicatePlayerError, PlayerNameFormatError, MatchNotFoundException
from src.templates.config_jinja import render_page


class ExceptionHandler:
    EXCEPTION = {
        NotFoundError: "404 Not Found",
        DuplicatePlayerError: "400 Bad Request",
        PlayerNameFormatError: "400 Bad Request",
        MatchNotFoundException: "400 Bad Request",

    }

    @classmethod
    def request_get(cls, environ, start_response):
        error = environ.get('exception')
        if type(error) in cls.EXCEPTION:
            status = cls.EXCEPTION.get(type(error))
            headers = [('Content-type', 'text/html; charset=utf-8')]
            start_response(status, headers)
            context = {
                "error": error,
            }
            rendered_html = render_page("exception.html", context)
            return [rendered_html.encode('utf-8')]
