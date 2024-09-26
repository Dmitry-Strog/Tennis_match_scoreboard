from urllib.parse import parse_qs

from src.service.new_match_service import NewMatchService


class NewMatchHandler:
    def __init__(self):
        self.service = NewMatchService()

    def request_get(self, start_response):
        status = "200 OK"
        headers = [('Content-type', 'text/html; charset=utf-8')]
        start_response(status, headers)
        with open("src/views/pages/index.html", "rb") as file:
            return [file.read()]

    def request_post(self, environ, start_response):
        content_length = int(environ.get('CONTENT_LENGTH', 0))
        post_data = environ['wsgi.input'].read(content_length).decode('utf-8')
        self.service.create_match(parse_qs(post_data))
        status = "201 CREATED"
        headers = [('Content-type', 'text/html; charset=utf-8')]
        start_response(status, headers)
        with open("src/views/pages/match-score.html", "rb") as file:
            return [file.read()]
