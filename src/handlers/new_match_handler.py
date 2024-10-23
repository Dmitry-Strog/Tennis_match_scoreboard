from urllib.parse import parse_qs

from src.service.data_access_or_storage.match_data import MatchData
from src.service.new_match_service import NewMatchService
from src.templates.config_jinja import render_page


class NewMatchHandler:
    def __init__(self):
        self.__service = NewMatchService()

    def request_get(self, start_response):
        status = "200 OK"
        headers = [('Content-type', 'text/html; charset=utf-8')]
        start_response(status, headers)
        rendered_html = render_page("new-match.html")
        return [rendered_html.encode('utf-8')]
        # with open("src/views/pages/index.html", "rb") as file:
        #     return [file.read()]

    def request_post(self, environ, start_response):
        content_length = int(environ.get('CONTENT_LENGTH', 0))
        post_data = environ['wsgi.input'].read(content_length).decode('utf-8')
        player1_name, player2_name = self.parse_url(post_data)

        match_data: MatchData = self.__service.start_match(player1_name, player2_name)
        uuid = match_data.uuid
        status = '303 See Other'
        headers = [('Location', f'/match-score?uuid={uuid}')]
        start_response(status, headers)
        return [b'Redirecting...']

    def parse_url(self, post_data):
        data = parse_qs(post_data)
        player1 = data["player1"]
        player2 = data["player2"]
        return player1, player2
