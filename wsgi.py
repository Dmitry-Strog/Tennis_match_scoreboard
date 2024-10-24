from waitress import serve

from src.handlers.finished_match_handler import FinishedMatchHandler
from src.handlers.match_score_handler import MatchScoreHandler
from src.handlers.new_match_handler import NewMatchHandler


class MainServer:
    def app(self, environ, start_response):
        request_uri = environ.get('PATH_INFO')
        request_method = environ.get('REQUEST_METHOD')
        if request_uri == "/new-match":
            handler = NewMatchHandler()

            if request_method == 'GET':
                response = handler.request_get(start_response)
                return response

            if request_method == 'POST':
                response = handler.request_post(environ, start_response)
                return response

        elif request_uri == "/match-score":
            handler = MatchScoreHandler()
            if request_method == 'GET':
                response = handler.request_get(environ, start_response)
                return response
            if request_method == 'POST':
                response = handler.request_post(environ, start_response)
                return response

        elif request_uri == "/matches":
            handler = FinishedMatchHandler()
            if request_method == 'GET':
                response = handler.request_get(environ, start_response)
                return response

        elif request_uri.startswith("/static/css"):
            status = "200 OK"
            headers = [('Content-type', 'text/css; charset=utf-8')]
            start_response(status, headers)
            with open("src/views/static/css/styles.css", "rb") as file:
                return [file.read()]

        elif request_uri.startswith("/favicon.ico"):
            status = "200 OK"
            headers = [('Content-type', 'image/x-icon')]
            start_response(status, headers)
            with open("src/views/static/img/logo-tennis.png", "rb") as file:
                return [file.read()]


if __name__ == '__main__':
    start = MainServer()
    print("Сервер запущен")
    serve(start.app, host='127.0.0.1', port='8000')
