import re
from urllib.parse import parse_qs

from src.exceptions import DuplicatePlayerError, PlayerNameFormatError
from src.dto import MatchDTO, PlayersDTO
from src.service.interface.new_match_service import NewMatchService
from src.templates.config_jinja import render_page


class NewMatchHandler:
    def __init__(self, service: NewMatchService):
        self.__service = service

    @classmethod
    def request_get(cls, environ, start_response):
        status = "200 OK"
        headers = [('Content-type', 'text/html; charset=utf-8')]
        start_response(status, headers)
        rendered_html = render_page("new-match.html")
        return [rendered_html.encode('utf-8')]

    def request_post(self, environ, start_response):
        content_length = int(environ.get('CONTENT_LENGTH', 0))
        post_data = environ['wsgi.input'].read(content_length).decode('utf-8')

        player_name_1, player_name_2 = self.parse_url(post_data)

        if player_name_1 == player_name_2:
            raise DuplicatePlayerError

        if self.validate_player_name(player_name_1) is False or self.validate_player_name(player_name_2) is False:
            raise PlayerNameFormatError

        match_dto: MatchDTO = self.__service.start_match(PlayersDTO(player_name_1, player_name_2))
        uuid = match_dto.uuid
        status = '303 See Other'
        headers = [('Location', f'/match-score?uuid={uuid}')]
        start_response(status, headers)
        return [b'Redirecting...']

    @staticmethod
    def parse_url(post_data) -> tuple:
        data = parse_qs(post_data)
        player1 = data["player1"][0]
        player2 = data["player2"][0]
        return player1, player2

    @staticmethod
    def validate_player_name(player_name):
        player_name = player_name.strip()
        pattern = r'^[a-zA-Zа-яА-Я0-9_\-\. ]+$'
        if re.match(pattern, player_name):
            return True
        else:
            return False
