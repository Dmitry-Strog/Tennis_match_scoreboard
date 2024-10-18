from urllib.parse import parse_qs

from src.service.match_data import MatchData
from src.service.match_score_service import MatchScoreService
from src.templates.config_jinja import render_page


class MatchScoreHandler:
    def __init__(self):
        self.service = MatchScoreService()

    def request_get(self, environ, start_response):
        status = "200 OK"
        headers = [('Content-type', 'text/html; charset=utf-8')]
        uuid = parse_qs(environ['QUERY_STRING'])["uuid"][0]
        match: MatchData = self.service.play_match(uuid)
        player1, player2 = match.score.keys()
        print(player1, player2)
        start_response(status, headers)

        context = {
            "uuid": uuid,
            "player1": player1,
            "player2": player2,
            "score": match.score,
        }

        rendered_html = render_page("match-score.html", context)
        return [rendered_html.encode('utf-8')]


    # def request_post(self, environ, start_response):
    #     content_length = int(environ.get('CONTENT_LENGTH', 0))
    #     post_data = environ['wsgi.input'].read(content_length).decode('utf-8')
    #     player1_name, player2_name = self.parse_url(post_data)
    #     match_data: MatchData = self.service.start_match(player1_name, player2_name)
    #     uuid = match_data.uuid
    #     status = '303 See Other'
    #     headers = [('Location', f'/match-score?uuid={uuid}')]
    #     start_response(status, headers)
    #     return [b'Redirecting...']
    #
    # def parse_url(self, post_data):
    #     data = parse_qs(post_data)
    #     player1 = data["player1"]
    #     player2 = data["player2"]
    #     return player1, player2