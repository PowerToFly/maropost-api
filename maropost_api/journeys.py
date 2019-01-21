from base import MaropostBase


class MaropostJourney(MaropostBase):

    def all(self):
        page = 1
        total_pages = 2
        while page < total_pages:
            result = self.get_journeys_from_page(page)
            if result:
                total_pages = result[0].get('total_pages') + 1
            page += 1
            yield result

    def get_journeys_from_page(self, page=1):
        response = self.browser.get('/journeys.json', params={'page': page})
        return self.validator(response).validate()

    def contacts(self, journey_id):
        page = 1
        total_pages = 2
        while page < total_pages:
            result = self.get_contacts_from_page(journey_id, page)
            if result:
                total_pages = result[0].get('total_pages') + 1
            page += 1
            yield result

    def get_contacts_from_page(self, journey_id, page=1):
        response = self.browser.get('/journeys/{}/journey_contacts.json'.format(journey_id), params={'page': page})
        return self.validator(response).validate()

    def stop_all_journeys(self, uid_or_email):
        params = {}
        if '@' in uid_or_email:
            params['email'] = uid_or_email.replace('+', '%2B')
        elif str(uid_or_email).isdigit():
            params['contact_id'] = uid_or_email
        else:
            params['uid'] = uid_or_email
        response = self.browser.put('/journeys/stop_all_journeys.json', params=params)
        return self.validator(response).validate()

    def stop_journey_for_contact(self, journey_id, uid_or_email):
        if '@' in uid_or_email:
            link = '/journeys/{}/stop/email.json?email={}'.format(journey_id, uid_or_email.replace('+', '%2B'))
        elif str(uid_or_email).isdigit():
            link = '/journeys/{}/stop/contact_id.json'.format(journey_id, uid_or_email)
        else:
            link = '/journeys/{}/stop/uid.json?uid={}'.format(journey_id, uid_or_email)
        response = self.browser.put(link)
        return self.validator(response).validate()

    def start_journey_for_contact(self, journey_id, uid_or_email):
        if '@' in uid_or_email:
            link = '/journeys/{}/start/email.json?email={}'.format(journey_id, uid_or_email.replace('+', '%2B'))
        elif str(uid_or_email).isdigit():
            link = '/journeys/{}/start/contact_id.json'.format(journey_id, uid_or_email)
        else:
            link = '/journeys/{}/start/uid.json?uid={}'.format(journey_id, uid_or_email)
        response = self.browser.put(link)
        return self.validator(response).validate()

    def reset_journey_for_contact(self, journey_id, uid_or_email):
        if '@' in uid_or_email:
            link = '/journeys/{}/reset/email.json?email={}'.format(journey_id, uid_or_email.replace('+', '%2B'))
        elif str(uid_or_email).isdigit():
            link = '/journeys/{}/reset/contact_id.json'.format(journey_id, uid_or_email)
        else:
            link = '/journeys/{}/reset/uid.json?uid={}'.format(journey_id, uid_or_email)
        response = self.browser.put(link)
        return self.validator(response).validate()
