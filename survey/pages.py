from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player

import datetime
import time

page1 = ["Page1affirm1", "Page1affirm2", "Page1affirm3", "Page1affirm4", "Page1affirm5", "Page1affirm6", "Page1affirm7"]
page2 = ["Page2healthM1", "Page2healthM2", "Page2healthM3", "Page2healthM4", "Page2healthM5", "Page2healthM6", "Page2healthM7"]
page3 = ["Page3healthT1", "Page3healthT2", "Page3healthT3", "Page3healthT4", "Page3healthT5", "Page3healthT6", "Page3healthT7"]
page4 = ["Page4mood1", "Page4mood2", "Page4mood3", "Page4mood4", "Page4mood5", "Page4mood6", "Page4mood7"]
page5 = ["accel1", "accel2", "accel3", "accel4", "accel5", "accel6", "accel7"]
page6 = ["help1", "help2", "help3", "help4", "help5", "help6", "help7"]

class PreTrial(Page):
    timeout_seconds = 5
    def before_next_page(self):
        self.player.daysurv = -1

class Start(Page):
    form_model = 'player'
    form_fields = ['valueP1', 'valueP2']

    # def before_next_page(self):
    #     self.participant.vars['expiry'] = time.time() + 1 * 60

class Wait(Page):
    form_model = 'player'

    #timeout_seconds = 10

    #timer_text = "See you tomorrow!"
    #timeout_seconds = 10
    # time = datetime.now()
    # form_fields = [time]

class Next(Page):
    form_model = 'player'

class Intro(Page):
    form_model = 'player'

    def before_next_page(self):
        self.player.daysurv = self.player.daysurv + 1

    # def get_timeout_seconds(self):
    #     return self.participant.vars['expiry'] - time.time()
    #
    # def is_displayed(self):
    #     return self.get_timeout_seconds() > 3

class MyPage(Page):
    form_model = 'player'
    form_fields = page1[int(self.player.daysurv)]

    def vars_for_template(self):
        valueP1 = self.player.valueP1
        return dict(
            valueP1 = valueP1
        )

    # def get_timeout_seconds(self):
    #     return self.participant.vars['expiry'] - time.time()
    #
    # def is_displayed(self):
    #     return self.get_timeout_seconds() > 3

class MyPage2(Page):
    form_model = 'player'
    form_fields = page2[int(self.player.daysurv)]

    def vars_for_template(self):
        valueP2 = self.player.valueP2
        return dict(
            valueP2 = valueP2
        )

    # def get_timeout_seconds(self):
    #     return self.participant.vars['expiry'] - time.time()
    #
    # def is_displayed(self):
    #     return self.get_timeout_seconds() > 3

class MyPage3(Page):
    form_model = 'player'
    form_fields = page3[int(self.player.daysurv)]
    #timeout_seconds = 60

    # def get_timeout_seconds(self):
    #     return self.participant.vars['expiry'] - time.time()
    #
    # def is_displayed(self):
    #     return self.get_timeout_seconds() > 3

class MyPage4(Page):
    form_model = 'player'
    form_fields = page4[int(self.player.daysurv)]

    # def get_timeout_seconds(self):
    #     return self.participant.vars['expiry'] - time.time()
    #
    # def is_displayed(self):
    #     return self.get_timeout_seconds() > 3

class MyPage5(Page):
    form_model = 'player'
    form_fields = page5[int(self.player.daysurv)]

class MyPage6(Page):
    form_model = 'player'
    form_fields = page6[int(self.player.daysurv)]

class Results(Page):
    pass


page_sequence = [PreTrial, Start, Intro, MyPage, MyPage2, MyPage3, MyPage4, MyPage5, MyPage6, Wait,
                 Intro, MyPage, MyPage2, MyPage3, MyPage4, MyPage5, MyPage6, Wait,
                 Intro, MyPage, MyPage2, MyPage3, MyPage4, MyPage5, MyPage6, Wait,
                 Intro, MyPage, MyPage2, MyPage3, MyPage4, MyPage5, MyPage6, Wait,
                 Intro, MyPage, MyPage2, MyPage3, MyPage4, MyPage5, MyPage6, Wait,
                 Intro, MyPage, MyPage2, MyPage3, MyPage4, MyPage5, MyPage6, Wait,
                 Intro, MyPage, MyPage2, MyPage3, MyPage4, MyPage5, MyPage6, Wait,
                 Intro, MyPage, MyPage2, MyPage3, MyPage4, MyPage5, MyPage6, Wait,
                 Intro, MyPage, MyPage2, MyPage3, MyPage4, MyPage5, MyPage6, Wait,
                 Intro, MyPage, MyPage2, MyPage3, MyPage4, MyPage5, MyPage6, Wait,
                 Intro, MyPage, MyPage2, MyPage3, MyPage4, MyPage5, MyPage6, Wait]
# , Start, Intro, MyPage, MyPage2, MyPage4, Wait, Next,
#                  Intro, MyPage, MyPage2, Wait, Next,
#                  Intro, MyPage, MyPage2, Wait, Next,
#                  Intro, MyPage, MyPage2]
