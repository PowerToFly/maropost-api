from .base import MaropostBase


class MaropostDoNotMailList(MaropostBase):

    def all_info(self):
        return self.pagination(self.get_info_from_page)

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

    def unsubscribe_contact_by_email(self, email):
        data = dict(global_unsubscribe=dict(email=email))
        return self.unsubscribe_contact(data)

    def unsubscribe_contact_by_uid(self, uid):
        data = dict(global_unsubscribe=dict(uid=uid))
        return self.unsubscribe_contact(data)

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
        return self.pagination(self.get_info_from_page)

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

    def unsubscribe_contact_by_email(self, email, brand_id):
        data = dict(brand_unsubscribe=dict(email=email, brand_id=brand_id))
        return self.unsubscribe_contact(data)

    def unsubscribe_contact_by_uid(self, uid, brand_id):
        data = dict(brand_unsubscribe=dict(uid=uid, brand_id=brand_id))
        return self.unsubscribe_contact(data)

    def find_by_email(self, email):
        response = self.browser.get('/brand_unsubscribes/email.json?email={}'.format(email.replace('+', '%2B')))
        return self.validator(response).validate()

    def find_by_email_in_brand(self, email, brand_name):
        response = self.browser.get('/brand_unsubscribes/email.json?email={}&brand={}'.format(email.replace('+', '%2B'), brand_name))
        return self.validator(response).validate()

    def delete_by_email_from_brand(self, email, brand_name):
        response = self.browser.delete('/brand_unsubscribes/delete.json?email={}&brand={}'.format(email.replace('+', '%2B'), brand_name))
        return self.validator(response).validate()

    def delete_by_email_brand_id_from_brand(self, email, brand_id):
        response = self.browser.delete('/brand_unsubscribes/delete.json?email={}&brand_id={}'.format(email.replace('+', '%2B'), brand_id))
        return self.validator(response).validate()

    def delete_by_email_from_all_brands(self, email):
        response = self.browser.delete('/brand_unsubscribes/delete.json?email={}'.format(email.replace('+', '%2B')))
        return self.validator(response).validate()
