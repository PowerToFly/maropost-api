from base import MaropostBase


class MaropostDoNotMailList(MaropostBase):

    def all_info(self):
        page = 1
        total_pages = 2
        while page < total_pages:
            result = self.get_info_from_page(page)
            if result:
                total_pages = result[0].get('total_pages') + 1
            page += 1
            yield result

    def get_info_from_page(self, page=1):
        response = self.browser.get('/global_unsubscribes/list.json', params={'page': page})
        return self.validator(response).validate()

    def unsubscribe_contact(self, data, **kwargs):
        """
        can be used uid or email
        example:
        {
          "global_unsubscribe": {
            "uid": "abcd",
            "email": "demo@email.com",
          }
        }
        """
        response = self.browser.post('/global_unsubscribes.json', data=data, **kwargs)
        return self.validator(response).validate()

    def find_by_email(self, email):
        response = self.browser.get('/global_unsubscribes/email.json?contact[email]={}'.format(email.replace('+', '%2B')))
        return self.validator(response).validate()

    def find_by_uid(self, uid):
        response = self.browser.get('/global_unsubscribes/email.json?uid={}'.format(uid))
        return self.validator(response).validate()

    def delete_by_email(self, email):
        response = self.browser.delete('/global_unsubscribes/delete.json?email={}'.format(email.replace('+', '%2B')))
        return self.validator(response).validate()

    def delete_by_uid(self, uid):
        response = self.browser.delete('/global_unsubscribes/delete.json?uid={}'.format(uid))
        return self.validator(response).validate()


class MaropostBrandDoNotMailList(MaropostBase):

    def all_info(self):
        page = 1
        total_pages = 2
        while page < total_pages:
            result = self.get_contacts_from_page(page)
            if result:
                total_pages = result[0].get('total_pages') + 1
            page += 1
            yield result

    def get_info_from_page(self, page=1):
        response = self.browser.get('/brand_unsubscribes.json', params={'page': page})
        return self.validator(response).validate()

    def unsubscribe_contact(self, data, **kwargs):
        """
        can be used uid or email and brand_name or brand_id
        example:
        {
          "brand_unsubscribe": {
            "uid": "abcd",
            "email": "demo@email.com",
            "brand_name": "brand_1",
            "brand_id": "brand_id"
          }
        }
        """
        response = self.browser.post('/brand_unsubscribes.json', data=data, **kwargs)
        return self.validator(response).validate()

    def find_by_email(self, email):
        response = self.browser.get('/brand_unsubscribes/email.json?email={}'.format(email.replace('+', '%2B')))
        return self.validator(response).validate()

    def find_by_email_in_brand(self, email, brand_name):
        response = self.browser.get('/brand_unsubscribes/email.json?email={}&brand={}'.format(email.replace('+', '%2B'), brand_name))
        return self.validator(response).validate()

    def delete_by_email_from_brand(self, email, brand_name):
        response = self.browser.delete('/brand_unsubscribes/delete.json?email={}&brand={}'.format(email.replace('+', '%2B'), brand_name))
        return self.validator(response).validate()
