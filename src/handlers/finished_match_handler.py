from urllib.parse import parse_qs

from src.service.data_access_or_storage.match_data import MatchData
from src.service.finished_match_service import FinishedMatchService
from src.templates.config_jinja import render_page


class FinishedMatchHandler:
    def __init__(self):
        self.__service = FinishedMatchService()

    def request_get(self, environ, start_response):
        status = "200 OK"
        headers = [('Content-type', 'text/html; charset=utf-8')]
        filter_name = self.parse_url(environ['QUERY_STRING'])
        match_list = self.__service.get_match(filter_name)
        start_response(status, headers)

        context = {
            "match_list": match_list,
        }

        rendered_html = render_page("matches.html", context)
        return [rendered_html.encode('utf-8')]

    def parse_url(self, post_data):
        data = parse_qs(post_data)
        if data:
            filter_name = data["filter_by_player_name"]
            return filter_name[0]
