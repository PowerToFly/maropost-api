import requests
import json
from time import sleep


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
            return MaropostBrowser.call_api(upper_name, self.make_uri(endpoint), **kwargs)
        return f

    @staticmethod
    def call_api(upper_name, endpoint, **kwargs):
        """API functions call wrapper for catch random HTTP error on Maropost,
        in case of 500 error, API call will be repeated 2 times with small delay
        """
        def f(method_name, api_endpoint, **fkwargs):
            response = requests.request(method_name, api_endpoint, **fkwargs)
            if response.status_code == 500:
                if f.__dict__.get('num_of_attempts', 1) < 3:
                    # little bit delay before next call
                    sleep((100 / 1000) * f.__dict__.get('num_of_attempts', 1))
                    f.num_of_attempts = f.__dict__.get('num_of_attempts', 1) + 1
                    return f(method_name, api_endpoint, **fkwargs)
            return response
        return f(upper_name, endpoint, **kwargs)
