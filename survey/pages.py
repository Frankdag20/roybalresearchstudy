from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import datetime

# currentDT = datetime.datetime.now()


class Start(Page):
    form_model = 'player'
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        import time
        # user has 5 minutes to complete as many pages as possible
        self.participant.vars['expiry'] = time.time() + 1 * 60

class Wait(Page):
    form_model = 'player'
    timer_text = "See you tomorrow!"
    timeout_seconds = 10
    # time = datetime.now()
    # form_fields = [time]

class Intro(Page):
    form_model = 'player'

class MyPage(Page):
    form_model = 'player'
    form_fields = ['affirm1']#, 'affirm2', 'affirm3']
#    def get_timeout_seconds(self):
#        return self.participant.vars['expiry'] - time.time()

#    def is_displayed(self):
#        return self.get_timeout_seconds() > 3

class MyPage2(Page):
    form_model = 'player'
    form_fields = ['healthP1']#, 'healthP2', 'healthP3']

class MyPage3(Page):
    form_model = 'player'
    form_fields = ['info3']
    #timeout_seconds = 60

class MyPage4(Page):
    form_model = 'player'
    form_fields = ['info4']

class MyPage5(Page):
    form_model = 'player'
    form_fields = ['info5', 'info6', 'info7', 'info8', 'info9']


class Results(Page):
    pass


page_sequence = [Intro, MyPage, MyPage2, Wait,
                 Intro, MyPage, MyPage2, Wait,
                 Intro, MyPage, MyPage2, Wait,
                 Intro, MyPage, MyPage2, Wait]
