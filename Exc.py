class NumberIsTooLargeException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class NumberIsLessThenZero(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message   

class InvalidObject(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message   
