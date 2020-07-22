class MaropostBase(object):
    def __init__(self, browser, validator):
        self.browser = browser
        self.validator = validator

    def pagination(self, func, **kwargs):
        page = 1
        total_pages = 2
        while page < total_pages:
            kwargs['page'] = page
            result = func(**kwargs)
            if result:
                total_pages = result[0].get('total_pages') + 1
            page += 1
            yield result