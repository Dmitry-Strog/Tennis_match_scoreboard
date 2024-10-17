from src.templates.config_jinja import render_page


class MatchScoreHandler:

    def request_get(self, start_response):
        status = "200 OK"
        headers = [('Content-type', 'text/html; charset=utf-8')]
        start_response(status, headers)

        rendered_html = render_page("match-score.html")
        return [rendered_html.encode('utf-8')]
        # with open("src/views/pages/match-score.html", "rb") as file:
        #     return [file.read()]

