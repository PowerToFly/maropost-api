from .base import MaropostBase


class MaropostJourney(MaropostBase):

    def all(self):
        return self.pagination(self.get_journeys_from_page)

    def get_journeys_from_page(self, page=1, no_counts=True):
        response = self.browser.get('/journeys.json', params={'page': page, 'no_counts': no_counts})
        return self.validator(response).validate()

    def contacts(self, journey_id):
        return self.pagination(self.get_contacts_from_page, journey_id=journey_id)

    def get_contacts_from_page(self, journey_id, page=1):
        response = self.browser.get('/journeys/{}/journey_contacts.json'.format(journey_id), params={'page': page})
        return self.validator(response).validate()

    def stop_all_journeys_for_contact_by_id(self, contact_id):
        response = self.browser.put('/journeys/stop_all_journeys.json?contact_id={}'.format(contact_id))
        return self.validator(response).validate()

    def stop_all_journeys_for_contact_by_email(self, email):
        response = self.browser.put('/journeys/stop_all_journeys.json?email={}'.format(email))
        return self.validator(response).validate()

    def stop_journey_for_contact_by_id(self, journey_id, contact_id):
        response = self.browser.put('/journeys/{}/stop/{}.json'.format(journey_id, contact_id))
        return self.validator(response).validate()

    def start_journey_for_contact_by_id(self, journey_id, contact_id):
        response = self.browser.put('/journeys/{}/start/{}.json'.format(journey_id, contact_id))
        return self.validator(response).validate()
