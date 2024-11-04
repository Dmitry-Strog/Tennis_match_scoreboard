class NotFoundHandler(Exception):
    def __init__(self):
        self.message = f"Not Path"

    def __str__(self):
        return self.message
