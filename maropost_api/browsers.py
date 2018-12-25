import requests
import json


class MaropostBrowser(object):

    def __init__(self, account_id, auth_token):
        self.set_default_config(account_id, auth_token)

    def set_default_config(self, account_id, auth_token):
        self.auth_token = auth_token
        self.set_base_url(account_id)

    def set_base_url(self, account_id):
        self.base_url = 'http://api.maropost.com/accounts/{}'.format(account_id)

    def make_uri(self, endpoint):
        return self.base_url + endpoint

    def __getattr__(self, name):
        def f(endpoint, data=None, **kwargs):
            upper_name = name.upper()
            if upper_name not in ('GET', 'POST', 'PUT', 'PATCH', 'HEAD',
                                  'DELETE', 'OPTIONS', 'CONNECT'):
                return name
            if 'headers' in kwargs:
                kwargs['headers']['Content-Type'] = 'application/json'
            else:
                kwargs['headers'] = {'Content-Type': 'application/json'}
            if data:
                kwargs['data'] = json.dumps(data)
            if 'params' in kwargs:
                kwargs['params'].update({'auth_token': self.auth_token})
            else:
                kwargs['params'] = {'auth_token': self.auth_token}
            return requests.request(upper_name, self.make_uri(endpoint), **kwargs)
        return f
