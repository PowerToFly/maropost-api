from cached_property import cached_property
from browsers import MaropostBrowser
from contacts import MaropostContact
from lists import MaropostList
from do_not_mail_lists import MaropostBrandDoNotMailList, MaropostDoNotMailList
from validators import MaropostValidator


class Maropost(object):
    def __init__(self, account_id, auth_token, browser=None, validator=None):
        self.browser = browser or MaropostBrowser(account_id, auth_token)
        self.validator = validator or MaropostValidator()

    @cached_property
    def contacts(self):
        """:rtype MaropostContact"""
        return MaropostContact(self.browser, self.validator)

    @cached_property
    def lists(self):
        """:rtype MaropostList"""
        return MaropostList(self.browser, self.validator)

    @property
    def brand_do_not_mail_lists(self):
        """:rtype MaropostBrandDoNotMailList"""
        return MaropostBrandDoNotMailList(self.browser, self.validator)

    @property
    def do_not_mail_list(self):
        """:rtype MaropostDoNotMailList"""
        return MaropostDoNotMailList(self.browser, self.validator)
