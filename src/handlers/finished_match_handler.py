from urllib.parse import parse_qs

from src.dao.match_dao import MatchDao
from src.service.pagination import Pagination
from src.templates.config_jinja import render_page


class FinishedMatchHandler:
    def __init__(self):
        self.__dao = MatchDao()

    @classmethod
    def parse_url(cls, post_data):
        data = parse_qs(post_data)
        if data:
            return {key: value[0] if len(value) == 1 else value for key, value in data.items()}
        return {}

    def request_get(self, environ, start_response):
        filter_by_player_name = None
        number_page = 1
        parsed_data = self.parse_url(environ['QUERY_STRING'])

        if parsed_data.get('filter_by_player_name', False):
            filter_by_player_name = parsed_data['filter_by_player_name']

        if parsed_data.get('page', False):
            try:
                number_page = int(parsed_data['page'])
            except ValueError:
                number_page = 1

        match_list = self.__dao.get_finished_match(filter_by_player_name)
        pagination = Pagination(match_list, number_page)

        context = {
            "page": pagination,
            "filter_by_player_name": filter_by_player_name,
        }

        status = "200 OK"
        headers = [('Content-type', 'text/html; charset=utf-8')]
        start_response(status, headers)

        rendered_html = render_page("matches.html", context)

        return [rendered_html.encode('utf-8')]
