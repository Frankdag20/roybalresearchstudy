from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Start(Page):
    form_model = 'player'
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        import time
        # user has 5 minutes to complete as many pages as possible
        self.participant.vars['expiry'] = time.time() + 1 * 60

class Wait(WaitPage):
    template_name = 'your_app_name/MyWaitPage.html'

class MyPage(Page):
    form_model = 'player'
    form_fields = ['info1', 'info2']
    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3

class MyPage2(Page):
    form_model = 'player'
    form_fields = ['info3', 'info2']
    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3

class MyPage3(Page):
    form_model = 'player'
    form_fields = ['info1', 'info4']
    #timeout_seconds = 60
    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3

class MyPage4(Page):
    form_model = 'player'
    form_fields = ['info1', 'info2']
    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3

class MyPage5(Page):
    form_model = 'player'
    form_fields = ['info1', 'info2']
    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3


class Results(Page):
    pass


page_sequence = [MyPage, Wait, MyPage2, Wait, MyPage3, Wait, MyPage4, Wait, MyPage5, Wait]
