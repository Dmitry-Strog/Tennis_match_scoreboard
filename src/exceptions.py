class TennisError(Exception):
    def __init__(self):
        self.message = f"Запрашиваемая страница не существует"

    def __str__(self):
        return self.message


class NotFoundError(TennisError):
    def __init__(self):
        self.message = f"Запрашиваемая страница не существует"


class DuplicatePlayerError(TennisError):
    def __init__(self):
        self.message = f"Игроки имеют одинаковые имена"


class PlayerNameFormatError(TennisError):
    def __init__(self):
        self.message = f"Недопустимый формат имени игрока"
