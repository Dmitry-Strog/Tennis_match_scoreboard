from src.dependency_config import configure_new_match, configure_match_score, configure_finished_match
from src.exceptions import NotFoundError
from src.handlers.exception_handler import ExceptionHandler
from src.handlers.finished_match_handler import FinishedMatchHandler
from src.handlers.index_handler import IndexHandler
from src.handlers.match_score_handler import MatchScoreHandler
from src.handlers.new_match_handler import NewMatchHandler


class MainServer:
    def __call__(self, environ, start_response):
        request_uri = environ.get('PATH_INFO')
        request_method = environ.get('REQUEST_METHOD')

        urls = {
            '/': IndexHandler,
            '/new-match': NewMatchHandler,
            '/match-score': MatchScoreHandler,
            '/matches': FinishedMatchHandler,
            '/exception': ExceptionHandler,
        }
        try:
            handler = urls.get(request_uri)
            if handler is None:
                raise NotFoundError

            handler = self.inject_dependency(handler)

            if request_method == 'GET':
                return handler.request_get(environ, start_response)

            elif request_method == 'POST':
                return handler.request_post(environ, start_response)
        except Exception as e:
            environ['exception'] = e
            handler = urls.get('/exception')
            return handler.request_get(environ, start_response)

    @staticmethod
    def inject_dependency(obj):
        if obj is NewMatchHandler:
            return configure_new_match()

        elif obj is MatchScoreHandler:
            return configure_match_score()

        elif obj is FinishedMatchHandler:
            return configure_finished_match()
        return obj
