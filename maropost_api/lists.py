from base import MaropostBase


class MaropostList(MaropostBase):

    def all(self):
        page = 1
        total_pages = 2
        while page < total_pages:
            result = self.get_lists_from_page(page)
            if result:
                total_pages = result[0].get('total_pages') + 1
            page += 1
            yield result

    def get_lists_from_page(self, page=1):
        response = self.browser.get('/lists.json', params={'page': page})
        return self.validator(response).validate()

    def get(self, list_id):
        response = self.browser.get('/lists/{}.json'.format(list_id))
        return self.validator(response).validate()

    def refresh(self, list_id):
        response = self.browser.get('/lists/{}/refresh_count.json'.format(list_id))
        return self.validator(response).validate()

    def create(self, data):
        response = self.browser.post('/lists.json', data)
        return self.validator(response).validate()

    def update(self, list_id, data):
        response = self.browser.put('/lists/{}.json'.format(list_id), data)
        return self.validator(response).validate()

    def ftp_update(self, list_id, data):
        response = self.browser.put('/lists/{}/ftp_import.json'.format(list_id), data)
        return self.validator(response).validate()

    def delete(self, list_id):
        response = self.browser.delete('/lists/{}.json'.format(list_id))
        return self.validator(response).validate()

    def contacts(self, list_id):
        page = 1
        total_pages = 2
        while page < total_pages:
            result = self.get_contacts_from_page(list_id, page)
            if result:
                total_pages = result[0].get('total_pages') + 1
            page += 1
            yield result

    def get_contacts_from_page(self, list_id, page=1):
        response = self.browser.get('/lists/{}/contacts.json'.format(list_id), params={'page': page})
        return self.validator(response).validate()