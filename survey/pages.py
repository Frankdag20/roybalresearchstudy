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
import calendar
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# import boto
# from boto.s3.connection import S3Connection
# user = S3Connection(os.environ['gmailUser'])
# password = S3Connection(os.environ['gmailPass'])
#
# from flask import Flask
# from flask_mail import Mail, Message
# import os
#
# app = Flask(__name__)
#
# mail_settings = {
#     "MAIL_SERVER": 'smtp.gmail.com',
#     "MAIL_PORT": 465,
#     "MAIL_USE_TLS": False,
#     "MAIL_USE_SSL": True,
#     "MAIL_USERNAME": user,
#     "MAIL_PASSWORD": password
# }
#
# app.config.update(mail_settings)
# mail = Mail(app)

import requests

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxbb6b4993235745c2bcf8f916e2671398.mailgun.org/messages",
        auth=("api", "5ef8144ae568ce778c28211951d26fb5-7cd1ac2b-169be750"),
        data={"from": "Excited User <sandboxbb6b4993235745c2bcf8f916e2671398.mailgun.org>",
              "to": ["fdagostinoj@gmail.com", "frankdag20@gmail.com"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})


def send_email(participant):
    #now = datetime.datetime.now()

    #today_date = datetime.date.today()  # today's date

    #cy = now.year  # current year
    #cm = now.month  # current month
    #cd = now.day  # current day
    # participant = participant + 1
    FROM = "fdagostinoj@gmail.com"
    # TO = ["frankdag20@gmail.com"]  # must be a list
    TO = ["frankdag20@gmail.com"]  # must be a list

    SUBJECT = "Hello!"
    TEXT = f"Hello, This is an automatic email notifying you that Participant {participant} has not yet filled out the survey for today."

    # Prepare actual message
    # message = """From: %s To: %s Subject: %s
    #
    # %s
    # """ % (FROM, ", ".join(TO), "Hello", TEXT)

    # Prepare actual message
    message = """Subject: %s

    %s
     """ % ("Research Notification", TEXT)

    # Send the mail
    username = str("fdagostinoj@gmail.com")
    password = str("dagostino1")

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
    # input("Press any key to exit..")

from datetime import datetime
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
        from datetime import datetime

        #self.participant.vars['day_of_experiment'] = 1
        # Datetime is 4 hours ahead of EDT
        self.participant.vars['expiry'] = int("29")
        print(self.participant.vars['expiry'])


class Start(Page):
    form_model = 'player'
    form_fields = ['valueP1', 'valueP2']

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")
        # Get day of the week

        if int(y) == 6:
            y = 30
        return (self.participant.vars['expiry'] - int(y))*3600

    def before_next_page(self):

        self.player.email_send()
        send_email(self.player.id_in_group)

    def is_displayed(self):

        return self.get_timeout_seconds() != 0

class Wait1(Page):
    form_model = 'player'

    def before_next_page(self):
        from datetime import datetime

        # Datetime is 4 hours ahead of EDT
        self.participant.vars['expiry'] = int("28")

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")
        # Get day of the week

        if int(y) == 6:
            y = 30

        #if int(y) == 18:
        #    self.participant.vars['day_of_experiment'] = 2

        #if self.participant.vars['day_of_experiment'] == 2:
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class Next(Page):
    form_model = 'player'

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")
        # Get day of the week
        day = 1
        if int(y) == 6:
            y = 30
        if self.participant.vars['day_of_experiment'] == 1:
            return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class Intro(Page):
    form_model = 'player'

    #with app.app_context():
    #    msg = Message(subject="Hello",
    #                  sender=user,
    #                  recipients=["frankdag20@gmail.com"],  # use your email for testing
    #                  body="This is a test email I sent with Gmail and Python!")
    #    mail.send(msg)

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        if int(y) == 6:
            y = 30

        return (self.participant.vars['expiry'] - int(y) - 1) * 3600

    def before_next_page(self):
        send_simple_message()
        send_email(self.player.id_in_group)

    def is_displayed(self):

        return self.get_timeout_seconds() != 0

class MyPage(Page):
    form_model = 'player'
    form_fields = [page1[0]]

    def vars_for_template(self):
        valueP1 = self.player.affirm_question
        return dict(
            valueP1 = valueP1
        )

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")
        # Get day of the week
        day = 1
        if int(y) == 6:
            y = 30
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
        x = datetime.now()
        y = x.strftime("%H")
        # Get day of the week
        day = 1
        if int(y) == 6:
            y = 30
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class MyPage3(Page):
    form_model = 'player'
    form_fields = ['Page3healthT']

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")
        # Get day of the week
        day = 1
        if int(y) == 6:
            y = 30
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

    #timeout_seconds = 60

    # def get_timeout_seconds(self):
    #     return self.participant.vars['expiry'] - time.time()
    #
    # def is_displayed(self):
    #     return self.get_timeout_seconds() > 3

class MyPage4(Page):
    form_model = 'player'
    form_fields = [page4[1]]

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")
        # Get day of the week
        day = 1
        if int(y) == 6:
            y = 30
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

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
        x = datetime.now()
        y = x.strftime("%H")
        # Get day of the week
        day = 1
        if int(y) == 6:
            y = 30
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class MyPage6(Page):
    form_model = 'player'
    form_fields = [page6[0]]

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")
        # Get day of the week
        day = 1
        if int(y) == 6:
            y = 30
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class Wait2(Page):
    form_model = 'player'

    def before_next_page(self):
        from datetime import datetime

        # Datetime is 4 hours ahead of EDT
        self.participant.vars['expiry'] = int("08")

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")
        # Get day of the week
        day = 1
        if int(y) == 6:
            y = 30

        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class Wait(Page):
    form_model = 'player'

    def before_next_page(self):
        from datetime import datetime

        # Datetime is 4 hours ahead of EDT
        self.participant.vars['expiry'] = int("08")

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")
        # Get day of the week
        day = 1
        if int(y) == 6:
            y = 30

        if int(y) == 6:
            self.participant.vars['day_of_experiment'] = 2

        if self.participant.vars['day_of_experiment'] == 2:
            return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class Results(Page):
    pass

# Was previously PreTrial, Start, Intro, MyPage, ...
page_sequence = [PreTrial, Intro, MyPage, MyPage2, MyPage3, MyPage4, MyPage5, MyPage6, Wait1,
                 Intro, MyPage, MyPage2, MyPage3, MyPage4, MyPage5, MyPage6, Wait2,
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
