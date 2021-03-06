from .base import MaropostBase


class MaropostContact(MaropostBase):

    def create(self, data, **kwargs):
        response = self.browser.post('/contacts.json', data, **kwargs)
        return self.validator(response).validate()

    def update(self, contact_id, data):
        response = self.browser.put('/contacts/{}.json'.format(contact_id), data)
        return self.validator(response).validate()

    def delete(self, email):
        response = self.browser.delete('/contacts/delete_all.json?contact[email]={}'.format(email))
        return self.validator(response).validate()

    def add_to_list(self, list_id, data, **kwargs):
        response = self.browser.post('/lists/{}/contacts.json'.format(list_id), data, **kwargs)
        return self.validator(response).validate()

    def update_in_list(self, contact_id, list_id, data):
        response = self.browser.put('/lists/{}/contacts/{}.json'.format(list_id, contact_id), data)
        return self.validator(response).validate()

    def remove_from_list(self, contact_id, list_id, **kwargs):
        response = self.browser.delete('/lists/{}/contacts/{}.json'.format(list_id, contact_id), **kwargs)
        return self.validator(response).validate()

    def remove_from_lists(self, contact_id, list_ids, **kwargs):
        response = self.browser.delete('/contacts/{}.json?list_ids={}'.format(contact_id, ','.join(str(v) for v in list_ids)), **kwargs)
        return self.validator(response).validate()

    def find_by_email(self, email):
        response = self.browser.get('/contacts/email.json?contact[email]={}'.format(email.replace('+', '%2B')))
        return self.validator(response).validate()

    def find_by_id(self, id):
        response = self.browser.get('/contacts/{}.json'.format(id))
        return self.validator(response).validate()

    def subscribe_to_lists(self, list_ids, data):
        response = self.browser.post('/contacts.json?list_ids={}'.format(','.join(list_ids)), data)
        return self.validator(response).validate()

    def unsubscribe_from_lists(self, contact_id, list_ids):
        response = self.browser.delete('/contacts/{}.json?list_ids={}'.format(contact_id, ','.join(map(str, list_ids))))
        return self.validator(response).validate()
