
class MaropostValidator(object):
    def __init__(self):
        pass

    def __call__(self, response):
        self.response = response
        return self

    def validate(self):
        return self.response.json()
