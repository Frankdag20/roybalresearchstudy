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
    if int(y) == 0:
        y = 24

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

def send_email_help(participant):

    FROM = "fdagostinoj@gmail.com"

    TO = ["frankdag20@gmail.com"]  # must be a list

    SUBJECT = "Hello!"
    TEXT = f"Hello, Participant {participant} has requested that someone reach out to them for assistance."

    message = """Subject: %s

    %s
     """ % (f"DASH: Participant {participant} is requesting assistance.", TEXT)

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

def check_notif_time(y):
    #stop = 0
    if int(y) > 12 and int(y) < 14:
        import smtplib
       # if stop == 0:
        send_email(self.player.id_in_group)
        #    stop = 1
        #stop = 1

class PreTrial(Page):
    form_model = 'player'
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        from datetime import datetime

        # Datetime is 4 hours ahead of EDT
        # Should be 29

        self.participant.vars['expiry'] = int("29")
        print(self.participant.vars['expiry'])

class Start(Page):
    form_model = 'player'
    form_fields = ['posOrNeg', 'affirmVal']

    def is_displayed(self):

        return self.get_timeout_seconds() != 0

########################################

class Intro_D1(Page):
    form_model = 'player'

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        y = fix_time(y)
        check_notif_time(y)

        return (self.participant.vars['expiry'] - int(y)-8) * 3600

    def before_next_page(self):
        self.participant.vars['expiry'] = int("29")

        self.player.time_begin_d1 = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        x = datetime.now()
        y = x.strftime("%H")

        y = fix_time(y)
        check_notif_time(y)
        if int(y) > 14 and int(y) < 16:
            import smtplib
            send_email(self.player.id_in_group)

    def is_displayed(self):

        return self.get_timeout_seconds() != 0

class MyPage_D1(Page):
    form_model = 'player'
    form_fields = ['affirm_D1']

    def vars_for_template(self):
        affirm_value = self.player.affirmVal
        return dict(
            disp_affirm_value = affirm_value
        )

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        y = fix_time(y)
        check_notif_time(y)
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

        self.player.seen_or_not = 1

        if health_message == False:
            disp = "If you stay inactive, you are more likely to die early. You may miss out on the people and things you love."
        if health_message == True:
            disp = "If you start to sit less, you are more likely to live longer. You will be able to enjoy the people and things you love."

        return dict(
            disp_health_message=disp
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

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class MyPage3_D1(Page):
    form_model = 'player'
    form_fields = ['conf_D1']

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class MyPage4_D1(Page):
    form_model = 'player'
    form_fields = ['mood_D1']

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class MyPage5_D1(Page):
    form_model = 'player'
    form_fields = ['help_D1']

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class Wait_D1(Page):
    form_model = 'player'

    def vars_for_template(self):
        assist = self.player.help_D1
        if assist == True:
            send_email_help(self.player.id_in_group)

        return dict(
            tip="Walk to music with a beat to improve your walking speed and rhythm."
        )

    def before_next_page(self):
        from datetime import datetime

        # Datetime is 4 hours ahead of EDT
        self.participant.vars['expiry'] = int("28")

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")
        # Get day of the week

        y = fix_time(y)

        return (self.participant.vars['expiry'] - int(y) + 1) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

########################################

class Intro_D2(Page):
    form_model = 'player'

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        y = fix_time(y)
        check_notif_time(y)

        return (self.participant.vars['expiry'] - int(y)-8) * 3600

    def before_next_page(self):
        self.player.time_begin_d1 = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.participant.vars['expiry'] = int("29")

        x = datetime.now()
        y = x.strftime("%H")

        y = fix_time(y)
        check_notif_time(y)

    def is_displayed(self):

        return self.get_timeout_seconds() != 0

class MyPage_D2(Page):
    form_model = 'player'
    form_fields = ['affirm_D2']

    def vars_for_template(self):
        affirm_value = self.player.affirmVal
        return dict(
            disp_affirm_value = affirm_value
        )

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        y = fix_time(y)
        check_notif_time(y)
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

class MyPage2_D2(Page):
    form_model = 'player'

    def vars_for_template(self):
        health_message = self.player.posOrNeg

        self.player.seen_or_not = 0

        if health_message == False:
            disp = "Inactive people often have higher blood sugar. Having high blood sugar can hurt your arteries."
        if health_message == True:
            disp = "Active people often have lower blood sugar. Having healthy blood sugar can protect your arteries."
        return dict(
            disp_health_message=disp
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

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class MyPage3_D2(Page):
    form_model = 'player'
    form_fields = ['conf_D2']

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class MyPage4_D2(Page):
    form_model = 'player'
    form_fields = ['mood_D2']

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class MyPage5_D2(Page):
    form_model = 'player'
    form_fields = ['help_D2']

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class Wait_D2(Page):
    form_model = 'player'

    def vars_for_template(self):
        assist = self.player.help_D2
        if assist == True:
            send_email_help(self.player.id_in_group)

        return dict(
            tip="Breathe in rhythm to your walking."
        )

    def before_next_page(self):
        from datetime import datetime

        # Datetime is 4 hours ahead of EDT
        self.participant.vars['expiry'] = int("28")

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")
        # Get day of the week

        y = fix_time(y)

        return (self.participant.vars['expiry'] - int(y) + 1) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

########################################

class Intro_D3(Page):
    form_model = 'player'

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        y = fix_time(y)
        check_notif_time(y)

        return (self.participant.vars['expiry'] - int(y)-8) * 3600

    def before_next_page(self):
        self.player.time_begin_d1 = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.participant.vars['expiry'] = int("29")

        x = datetime.now()
        y = x.strftime("%H")

        y = fix_time(y)
        check_notif_time(y)

    def is_displayed(self):

        return self.get_timeout_seconds() != 0

class MyPage_D3(Page):
    form_model = 'player'
    form_fields = ['affirm_D3']

    def vars_for_template(self):
        affirm_value = self.player.affirmVal
        return dict(
            disp_affirm_value = affirm_value
        )

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        y = fix_time(y)
        check_notif_time(y)
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

class MyPage2_D3(Page):
    form_model = 'player'

    def vars_for_template(self):
        health_message = self.player.posOrNeg

        self.player.seen_or_not = 0

        if health_message == False:
            disp = "If you don't walk enough, your bones will grow weaker. Weaker bones make you more likely to have pain."
        if health_message == True:
            disp = "If you spend time walking, your bones will grow stronger. Stronger bones will help you stay pain-free."
        return dict(
            disp_health_message=disp
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

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class MyPage3_D3(Page):
    form_model = 'player'
    form_fields = ['conf_D3']

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class MyPage4_D3(Page):
    form_model = 'player'
    form_fields = ['mood_D3']

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class MyPage5_D3(Page):
    form_model = 'player'
    form_fields = ['help_D3']

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class Wait_D3(Page):
    form_model = 'player'

    def vars_for_template(self):
        assist = self.player.help_D3
        if assist == True:
            send_email_help(self.player.id_in_group)

        return dict(
            tip="Walk free: don’t take too much with you when you walk, and keep your hands free."
      )

    def before_next_page(self):
        from datetime import datetime

        # Datetime is 4 hours ahead of EDT
        self.participant.vars['expiry'] = int("28")

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")
        # Get day of the week

        y = fix_time(y)

        return (self.participant.vars['expiry'] - int(y) + 1) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

########################################

class Intro_D4(Page):
    form_model = 'player'

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        y = fix_time(y)
        check_notif_time(y)

        return (self.participant.vars['expiry'] - int(y)-8) * 3600

    def before_next_page(self):
        self.player.time_begin_d4 = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.participant.vars['expiry'] = int("29")

        x = datetime.now()
        y = x.strftime("%H")

        y = fix_time(y)
        check_notif_time(y)

    def is_displayed(self):

        return self.get_timeout_seconds() != 0

class MyPage_D4(Page):
    form_model = 'player'
    form_fields = ['affirm_D4']

    def vars_for_template(self):
        affirm_value = self.player.affirmVal
        return dict(
            disp_affirm_value = affirm_value
        )

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        y = fix_time(y)
        check_notif_time(y)
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

class MyPage2_D4(Page):
    form_model = 'player'

    def vars_for_template(self):
        health_message = self.player.posOrNeg

        self.player.seen_or_not = 1

        if health_message == False:
            disp = "If you keep being inactive, you are more likely to get cancer. This means you may die earlier than if you were more active."
        if health_message == True:
            disp = "If you become more active, you are less likely to get cancer. This means you may live longer than if you were more inactive."
        return dict(
            disp_health_message=disp
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

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class MyPage3_D4(Page):
    form_model = 'player'
    form_fields = ['conf_D4']

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class MyPage4_D4(Page):
    form_model = 'player'
    form_fields = ['mood_D4']

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class MyPage5_D4(Page):
    form_model = 'player'
    form_fields = ['help_D4']

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class Wait_D4(Page):
    form_model = 'player'

    def vars_for_template(self):
        assist = self.player.help_D4
        if assist == True:
            send_email_help(self.player.id_in_group)

        return dict(
            tip="Keep a walking diary to track your progress."
        )

    def before_next_page(self):
        from datetime import datetime

        # Datetime is 4 hours ahead of EDT
        self.participant.vars['expiry'] = int("28")

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")
        # Get day of the week

        y = fix_time(y)

        return (self.participant.vars['expiry'] - int(y) + 1) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

########################################

class Intro_D5(Page):
    form_model = 'player'

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        y = fix_time(y)
        check_notif_time(y)

        return (self.participant.vars['expiry'] - int(y)-8) * 3600

    def before_next_page(self):
        self.player.time_begin_d1 = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.participant.vars['expiry'] = int("29")

        x = datetime.now()
        y = x.strftime("%H")

        y = fix_time(y)
        check_notif_time(y)

    def is_displayed(self):

        return self.get_timeout_seconds() != 0

class MyPage_D5(Page):
    form_model = 'player'
    form_fields = ['affirm_D5']

    def vars_for_template(self):
        affirm_value = self.player.affirmVal
        return dict(
            disp_affirm_value = affirm_value
        )

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        y = fix_time(y)
        check_notif_time(y)
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

class MyPage2_D5(Page):
    form_model = 'player'

    def vars_for_template(self):
        health_message = self.player.posOrNeg

        self.player.seen_or_not = 1

        if health_message == False:
            disp = "People who spend all of their time sitting are almost twice as likely to die from cancer than those who are very active."
        if health_message == True:
            disp = "People who are very active are about half as likely to die from cancer than those who spend all of their time sitting."
        return dict(
            disp_health_message=disp
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

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class MyPage3_D5(Page):
    form_model = 'player'
    form_fields = ['conf_D5']

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class MyPage4_D5(Page):
    form_model = 'player'
    form_fields = ['mood_D5']

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class MyPage5_D5(Page):
    form_model = 'player'
    form_fields = ['help_D5']

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class Wait_D5(Page):
    form_model = 'player'

    def vars_for_template(self):
        assist = self.player.help_D5
        if assist == True:
            send_email_help(self.player.id_in_group)

        return dict(
            tip="Don’t just “think” your walking goals, write them down."
        )

    def before_next_page(self):
        from datetime import datetime

        # Datetime is 4 hours ahead of EDT
        self.participant.vars['expiry'] = int("28")

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")
        # Get day of the week

        y = fix_time(y)

        return (self.participant.vars['expiry'] - int(y) + 1) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

########################################

class Intro_D6(Page):
    form_model = 'player'

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        y = fix_time(y)
        check_notif_time(y)

        return (self.participant.vars['expiry'] - int(y)-8) * 3600

    def before_next_page(self):
        self.player.time_begin_d1 = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.participant.vars['expiry'] = int("29")

        x = datetime.now()
        y = x.strftime("%H")

        y = fix_time(y)
        check_notif_time(y)

    def is_displayed(self):

        return self.get_timeout_seconds() != 0

class MyPage_D6(Page):
    form_model = 'player'
    form_fields = ['affirm_D6']

    def vars_for_template(self):
        affirm_value = self.player.affirmVal
        return dict(
            disp_affirm_value = affirm_value
        )

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        y = fix_time(y)
        check_notif_time(y)
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

class MyPage2_D6(Page):
    form_model = 'player'

    def vars_for_template(self):
        health_message = self.player.posOrNeg

        self.player.seen_or_not = 0

        if health_message == False:
            disp = "If you continue to be inactive, it is more difficult to digest food. This means you are more likely to get colon cancer."
        if health_message == True:
            disp = "If you become more active, it is easier to digest food.  This means you are less likely to get colon cancer."
        return dict(
            disp_health_message=disp
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

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class MyPage3_D6(Page):
    form_model = 'player'
    form_fields = ['conf_D6']

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class MyPage4_D6(Page):
    form_model = 'player'
    form_fields = ['mood_D6']

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class MyPage5_D6(Page):
    form_model = 'player'
    form_fields = ['help_D6']

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class Wait_D6(Page):
    form_model = 'player'

    def vars_for_template(self):
        assist = self.player.help_D6
        if assist == True:
            send_email_help(self.player.id_in_group)

        return dict(
            tip="Walk at an intensity that you can talk but not sing."
        )

    def before_next_page(self):
        from datetime import datetime

        # Datetime is 4 hours ahead of EDT
        self.participant.vars['expiry'] = int("28")

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")
        # Get day of the week

        y = fix_time(y)

        return (self.participant.vars['expiry'] - int(y) + 1) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

########################################

class Intro_D7(Page):
    form_model = 'player'

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        y = fix_time(y)
        check_notif_time(y)

        return (self.participant.vars['expiry'] - int(y)-8) * 3600

    def before_next_page(self):
        self.player.time_begin_d1 = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.participant.vars['expiry'] = int("29")

        x = datetime.now()
        y = x.strftime("%H")

        y = fix_time(y)
        check_notif_time(y)

    def is_displayed(self):

        return self.get_timeout_seconds() != 0

class MyPage_D7(Page):
    form_model = 'player'
    form_fields = ['affirm_D7']

    def vars_for_template(self):
        affirm_value = self.player.affirmVal
        return dict(
            disp_affirm_value = affirm_value
        )

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        y = fix_time(y)
        check_notif_time(y)
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

class MyPage2_D7(Page):
    form_model = 'player'

    def vars_for_template(self):
        health_message = self.player.posOrNeg

        self.player.seen_or_not = 0

        if health_message == False:
            disp = "People who are inactive have more of the hormones that help cancer grow. This means you are more likely to develop cancer."
        if health_message == True:
            disp = "People who become active have less of the hormones that help cancer grow. This means you are less likely to develop cancer."
        return dict(
            disp_health_message=disp
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

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class MyPage3_D7(Page):
    form_model = 'player'
    form_fields = ['conf_D7']

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class MyPage4_D7(Page):
    form_model = 'player'
    form_fields = ['mood_D7']

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class MyPage5_D7(Page):
    form_model = 'player'
    form_fields = ['help_D7']

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class Wait_D7(Page):
    form_model = 'player'

    def vars_for_template(self):
        assist = self.player.help_D7
        if assist == True:
            send_email_help(self.player.id_in_group)

        return dict(
            tip="Choose shoes with flat, supportive, flexible soles when you walk."
        )

    def before_next_page(self):
        from datetime import datetime

        # Datetime is 4 hours ahead of EDT
        self.participant.vars['expiry'] = int("28")

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")
        # Get day of the week

        y = fix_time(y)

        return (self.participant.vars['expiry'] - int(y) + 1) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0


class MyPage6_D1(Page):
    form_model = 'player'
    form_fields = [page5[0]]

    # Only show to P2
    #def is_displayed(self):
    #    return self.player.id_in_group == 2

    def vars_for_template(self):
        assist = self.player.help1
        if assist == True:
            send_email_help(self.player.id_in_group)

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class Results(Page):
    pass

# Init page sequence    # Intro_D1, MyPage_D1, MyPage2_D1, MyPage3_D1, MyPage4_D1, MyPage5_D1, Wait_D1,
   # Intro_D2, MyPage_D2, MyPage2_D2, MyPage3_D2, MyPage4_D2, MyPage5_D2, Wait_D2,
   # Intro_D3, MyPage_D3, MyPage2_D3, MyPage3_D3, MyPage4_D3, MyPage5_D3, Wait_D3
page_sequence = [PreTrial, Start, Intro_D4, MyPage_D4, MyPage2_D4, MyPage3_D4, MyPage4_D4, MyPage5_D4, Wait_D4,
                                Intro_D5, MyPage_D5, MyPage2_D5, MyPage3_D5, MyPage4_D5, MyPage5_D5, Wait_D5,
                                Intro_D6, MyPage_D6, MyPage2_D6, MyPage3_D6, MyPage4_D6, MyPage5_D6, Wait_D6,
                                Intro_D7, MyPage_D7, MyPage2_D7, MyPage3_D7, MyPage4_D7, MyPage5_D7, Wait_D7
                 ]
