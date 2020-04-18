class BaseCustomException(Exception):
    def __init__(self, message):
        self.message = message

    def json(self):
        return {"message": self.message}


class ParsingError(BaseCustomException):
    pass
