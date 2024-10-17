class MatchScoreHandler:

    def request_get(self, start_response):
        status = "200 OK"
        headers = [('Content-type', 'text/html; charset=utf-8')]
        start_response(status, headers)
        with open("src/views/pages/match-score.html", "rb") as file:
            return [file.read()]

