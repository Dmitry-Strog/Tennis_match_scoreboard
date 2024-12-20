from urllib.parse import parse_qs

from src.dto import MatchDTO
from src.service.interface.match_score_service import MatchScoreService
from src.templates.config_jinja import render_page


class MatchScoreHandler:
    def __init__(self, service: MatchScoreService):
        self.__service = service

    def request_get(self, environ, start_response):
        status = "200 OK"
        headers = [('Content-type', 'text/html; charset=utf-8')]
        uuid = parse_qs(environ['QUERY_STRING'])["uuid"][0]
        match: MatchDTO = self.__service.play_match(uuid)
        player1, player2 = match.score.keys()
        start_response(status, headers)

        context = {
            "uuid": uuid,
            "player1": player1,
            "player2": player2,
            "score": match.score,
            "winner": match.winner,
        }

        rendered_html = render_page("match-score.html", context)
        return [rendered_html.encode('utf-8')]

    def request_post(self, environ, start_response):
        content_length = int(environ.get('CONTENT_LENGTH', 0))
        post_data = environ['wsgi.input'].read(content_length).decode('utf-8')
        uuid, point = self.parse_url(post_data)
        status = '200 OK'
        headers = [('Content-type', 'text/html; charset=utf-8')]

        match: MatchDTO = self.__service.play_match(uuid, point)
        player1, player2 = match.score.keys()
        start_response(status, headers)

        context = {
            "uuid": uuid,
            "player1": player1,
            "player2": player2,
            "score": match.score,
            "winner": match.winner,
        }

        rendered_html = render_page("match-score.html", context)
        return [rendered_html.encode('utf-8')]

    def parse_url(self, post_data):
        data = parse_qs(post_data)
        uuid = data["uuid"]
        point = data["point"]
        return uuid[0], int(point[0])
