from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import datetime
import time

# currentDT = datetime.datetime.now()

class Start(Page):
    form_model = 'player'
    # def is_displayed(self):
    #     return self.round_number == 1
    #
    # def before_next_page(self):
    #     import time
    #     self.participant.vars['expiry'] = time.time() + 3 * 60

class Wait(Page):
    form_model = 'player'

    timeout_seconds = 10

    #timer_text = "See you tomorrow!"
    #timeout_seconds = 10
    # time = datetime.now()
    # form_fields = [time]

class Next(Page):
    form_model = 'player'

class Idle(Page):
    form_model = 'player'

    timeout_seconds = 5

class Intro(Page):
    form_model = 'player'

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3

class MyPage(Page):
    form_model = 'player'
    form_fields = ['Page1affirm']#, 'affirm2', 'affirm3']

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3

class MyPage2(Page):
    form_model = 'player'
    form_fields = ['Page2healthM']#, 'healthP2', 'healthP3']

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3

class MyPage3(Page):
    form_model = 'player'
    form_fields = ['Page3healthT']
    #timeout_seconds = 60

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3

class MyPage4(Page):
    form_model = 'player'
    form_fields = ['Page5mood']

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3

class MyPage5(Page):
    form_model = 'player'
    form_fields = ['info5', 'info6', 'info7', 'info8', 'info9']

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3

class Results(Page):
    pass


page_sequence = [Idle, Start, Intro, MyPage, MyPage2, MyPage4, Wait, Next,
                 Intro, MyPage, MyPage2, Wait, Next,
                 Intro, MyPage, MyPage2, Wait, Next,
                 Intro, MyPage, MyPage2]
