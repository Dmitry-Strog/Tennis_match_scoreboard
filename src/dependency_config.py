from src.handlers.finished_match_handler import FinishedMatchHandler
from src.handlers.match_score_handler import MatchScoreHandler
from src.handlers.new_match_handler import NewMatchHandler
from src.repository.match_repository_impl import MatchRepositoryImpl
from src.repository.player_repository_impl import PlayerRepositoryImpl
from src.service.match_score_service_impl import MatchScoreServiceImpl
from src.service.new_match_service_impl import NewMatchServiceImpl


def configure_new_match():
    player_repo = PlayerRepositoryImpl()
    match_repo = MatchRepositoryImpl()
    service = NewMatchServiceImpl(player_repo, match_repo)
    return NewMatchHandler(service)


def configure_match_score():
    player_repo = PlayerRepositoryImpl()
    match_repo = MatchRepositoryImpl()
    service = MatchScoreServiceImpl(player_repo, match_repo)
    return MatchScoreHandler(service)


def configure_finished_match():
    match_repo = MatchRepositoryImpl()
    return FinishedMatchHandler(match_repo)
