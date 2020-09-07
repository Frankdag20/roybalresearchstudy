#from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player
import smtplib
import os

from datetime import datetime
import time
import calendar
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

page1 = ['Page1affirm1', 'Page1affirm2', 'Page1affirm3', 'Page1affirm4', 'Page1affirm5', 'Page1affirm6', 'Page1affirm7']
page2 = ['Page2healthM1', 'Page2healthM2', 'Page2healthM3', 'Page2healthM4', 'Page2healthM5', 'Page2healthM6', 'Page2healthM7']
page3 = ['Page3healthT1', 'Page3healthT2', 'Page3healthT3', 'Page3healthT4', 'Page3healthT5', 'Page3healthT6', 'Page3healthT7']
page4 = ['Page4mood1', 'Page4mood2', 'Page4mood3', 'Page4mood4', 'Page4mood5', 'Page4mood6', 'Page4mood7']
page5 = ['accel1', 'accel2', 'accel3', 'accel4', 'accel5', 'accel6', 'accel7']
page6 = ['help1', 'help2', 'help3', 'help4', 'help5', 'help6', 'help7']

def fix_time(y):
    if int(y) == 1:
        y = 25

    if int(y) == 2:
        y = 26

    if int(y) == 3:
        y = 27

    if int(y) == 4:
        y = 28

    if int(y) == 5:
        y = 29

    if int(y) == 6:
        y = 30

    return y

def send_email(participant):

    FROM = "fdagostinoj@gmail.com"

    TO = ["frankdag20@gmail.com"]  # must be a list

    SUBJECT = "Hello!"
    TEXT = f"Hello, This is an automatic email notifying you that Participant {participant} has not yet filled out the survey for today."

    message = """Subject: %s

    %s
     """ % (f"DASH: Participant {participant} has not filled out survey.", TEXT)

    # Send the mail
    username = str("fdagostinoj@gmail.com")
    password = str("Dagostino1?")

    server = smtplib.SMTP("smtp.gmail.com", 587, timeout=30)
    server.set_debuglevel(1)

    try:
        server.starttls()
        server.login(username, password)
        server.sendmail(FROM, TO, message)
        print("The reminder e-mail for DASH was sent !")
    except:
        print("Couldn't send e-mail regarding DASH")
    finally:
        server.quit()

class PreTrial(Page):
    form_model = 'player'
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        from datetime import datetime

        # Datetime is 4 hours ahead of EDT

        self.participant.vars['expiry'] = int("29")
        print(self.participant.vars['expiry'])

class Start(Page):
    form_model = 'player'
    form_fields = ['posOrNeg', 'affirmVal']

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")
        # Get hour of the day

        y = fix_time(y)

        return (self.participant.vars['expiry'] - int(y))*3600

    def before_next_page(self):

        self.player.email_send()
        #send_email(self.player.id_in_group)

    def is_displayed(self):

        return self.get_timeout_seconds() != 0

class Wait(Page):
    form_model = 'player'

    def before_next_page(self):
        from datetime import datetime

        # Datetime is 4 hours ahead of EDT
        self.participant.vars['expiry'] = int("28")

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")
        # Get day of the week

        y = fix_time(y)

        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class Intro_D1(Page):
    form_model = 'player'

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        y = fix_time(y)

        if int(y) == 16:

            stop = 0
            import smtplib
            if stop == 0:
                send_email(self.player.id_in_group)
                stop = 1
            stop = 1

        return (self.participant.vars['expiry'] - int(y) - 1) * 3600

    def is_displayed(self):

        return self.get_timeout_seconds() != 0

class MyPage_D1(Page):
    form_model = 'player'
    form_fields = ['Page1affirm1']

    def vars_for_template(self):
        affirm_value = self.player.affirmVal
        return dict(
            disp_affirm_value = affirm_value
        )

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")
        # Get day of the week
        day = 1
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

    # def before_next_page(self):
        # self.player.notif()

    # form_fields = ['affirm_answer']
    #
    # def submitted_answer_choices(self):
    #     qd = self.player.get_value()
    #     return qd

class MyPage2_D1(Page):
    form_model = 'player'

    def vars_for_template(self):
        health_message = self.player.posOrNeg
        return dict(
            disp_health_message=health_message
        )

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
        x = datetime.now()
        y = x.strftime("%H")
        # Get day of the week
        day = 1
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class MyPage3_D1(Page):
    form_model = 'player'
    form_fields = ['Page3healthT']

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class MyPage4_D1(Page):
    form_model = 'player'
    form_fields = [page4[1]]

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")
        # Get day of the week
        day = 1
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

    # def get_timeout_seconds(self):
    #     return self.participant.vars['expiry'] - time.time()
    #
    # def is_displayed(self):
    #     return self.get_timeout_seconds() > 3

class MyPage5_D1(Page):
    form_model = 'player'
    form_fields = [page5[0]]

    # Only show to P2
    #def is_displayed(self):
    #    return self.player.id_in_group == 2

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")
        # Get day of the week
        day = 1
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class MyPage6_D1(Page):
    form_model = 'player'
    form_fields = [page6[0]]

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")
        # Get day of the week
        day = 1
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class Results(Page):
    pass

# Init page sequence
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
