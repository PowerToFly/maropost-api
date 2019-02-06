from base import MaropostBase


class MaropostReport(MaropostBase):

    def get_bounces(self, **kwargs):
        response = self.browser.get('/reports/bounces.json', params=kwargs)
        return self.validator(response).validate()

    def get_complaints(self, **kwargs):
        response = self.browser.get('/reports/complaints.json', params=kwargs)
        return self.validator(response).validate()
