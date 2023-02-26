class Errors(Exception):
    pass
class NameError(Errors):
    error_message = ('Invalid city name. City name must contain only letters')
    def __init__(self):
        super().__init__()
        self.msg = self.error_message
    def __str__(self):
        return self.msg

class UrlError(Errors):

    error_message = ("Invalid URL. Try again")
    def __init__(self):
        super().__init__()
        self.msg = self.error_message
    def __str__(self):
        return self.msg
class APIKeyError(Errors):

    error_message = ('Invalid URL. Try again')
    def __init__(self):
        super().__init__()
        self.msg = self.error_message
    def __str__(self):
        return self.msg


