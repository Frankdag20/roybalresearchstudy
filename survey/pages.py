#from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player
import datetime
import calendar
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# import sendEmail.py

# import importlib
# importlib.import_module('sendEmail')

import datetime
import time

page1 = ['Page1affirm1', 'Page1affirm2', 'Page1affirm3', 'Page1affirm4', 'Page1affirm5', 'Page1affirm6', 'Page1affirm7']
page2 = ['Page2healthM1', 'Page2healthM2', 'Page2healthM3', 'Page2healthM4', 'Page2healthM5', 'Page2healthM6', 'Page2healthM7']
page3 = ['Page3healthT1', 'Page3healthT2', 'Page3healthT3', 'Page3healthT4', 'Page3healthT5', 'Page3healthT6', 'Page3healthT7']
page4 = ['Page4mood1', 'Page4mood2', 'Page4mood3', 'Page4mood4', 'Page4mood5', 'Page4mood6', 'Page4mood7']
page5 = ['accel1', 'accel2', 'accel3', 'accel4', 'accel5', 'accel6', 'accel7']
page6 = ['help1', 'help2', 'help3', 'help4', 'help5', 'help6', 'help7']

class PreTrial(Page):
    form_model = 'player'
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        import time
        # user has 5 minutes to complete as many pages as possible
        self.player.vars['expiry'] = time.time() + 2 * 60
    # timeout_seconds = 5
    # def before_next_page(self):
        #self.player.daysurv = -1
        #self.player.track = self.player.id_in_group

class Start(Page):
    form_model = 'player'
    form_fields = ['valueP1', 'valueP2']

    def get_timeout_seconds(self):
        return self.player.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3
    # def before_next_page(self):
    #     self.participant.vars['expiry'] = time.time() + 1 * 60

class Wait(Page):
    form_model = 'player'

    #timeout_seconds = 10

    def get_timeout_seconds(self):
        return self.player.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3
    #timer_text = 'See you tomorrow!'
    #timeout_seconds = 10
    # time = datetime.now()
    # form_fields = [time]

class Next(Page):
    form_model = 'player'

    def get_timeout_seconds(self):
        return self.player.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3

class Intro(Page):
    form_model = 'player'

    def before_next_page(self):
        self.player.daysurv = self.player.daysurv + 1

    def get_timeout_seconds(self):
        return self.player.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3
    # def get_timeout_seconds(self):
    #     return self.participant.vars['expiry'] - time.time()
    #
    # def is_displayed(self):
    #     return self.get_timeout_seconds() > 3

class MyPage(Page):
    form_model = 'player'
    form_fields = [page1[0]]

    def vars_for_template(self):
        # self.player.valueP1
        valueP1 = self.player.affirm_question
        return dict(
            valueP1 = valueP1
        )

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3

    # def before_next_page(self):
        # self.player.notif()

    # form_fields = ['affirm_answer']
    #
    # def submitted_answer_choices(self):
    #     qd = self.player.get_value()
    #     return qd

    # def get_timeout_seconds(self):
    #     return self.participant.vars['expiry'] - time.time()
    #
    # def is_displayed(self):
    #     return self.get_timeout_seconds() > 3

class MyPage2(Page):
    form_model = 'player'
    # form_fields = [page2[0]]

    # def vars_for_template(self):
        # valueP2 = self.player.valueP2
        # return dict(
            # valueP2 = valueP2
        # )

    form_fields = ['submitted_answer']

    def submitted_answer_choices(self):
        qd = self.player.current_question()
        return [
            qd['CO'],
            qd['CN'],
            qd['UO'],
            qd['UN'],
        ]

    def before_next_page(self):
        self.player.check_correct()

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3
    # def get_timeout_seconds(self):
    #     return self.participant.vars['expiry'] - time.time()
    #
    # def is_displayed(self):
    #     return self.get_timeout_seconds() > 3

class MyPage3(Page):
    form_model = 'player'
    form_fields = ['Page3healthT']

    #timeout_seconds = 60

    # def get_timeout_seconds(self):
    #     return self.participant.vars['expiry'] - time.time()
    #
    # def is_displayed(self):
    #     return self.get_timeout_seconds() > 3

class MyPage4(Page):
    form_model = 'player'
    form_fields = [page4[1]]

    # def get_timeout_seconds(self):
    #     return self.participant.vars['expiry'] - time.time()
    #
    # def is_displayed(self):
    #     return self.get_timeout_seconds() > 3

class MyPage5(Page):
    form_model = 'player'
    form_fields = [page5[0]]

    # Only show to P2
    #def is_displayed(self):
    #    return self.player.id_in_group == 2

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3

class MyPage6(Page):
    form_model = 'player'
    form_fields = [page6[0]]

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3

class Results(Page):
    pass

# Was previously PreTrial, Start, Intro, MyPage, ...
page_sequence = [PreTrial, Intro, MyPage, MyPage2, MyPage3, MyPage4, MyPage5, MyPage6, Wait,
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
