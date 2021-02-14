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

affirm_array = ['affirm_D1', 'affirm_D2', 'affirm_D3', 'affirm_D4', 'affirm_D5', 'affirm_D6', 'affirm_D7', 'affirm_D8', 'affirm_D9', 'affirm_D10', 'affirm_D11', 'affirm_D12', 'affirm_D13', 'affirm_D14', 'affirm_D15', 'affirm_D16', 'affirm_D17', 'affirm_D18', 'affirm_D19', 'affirm_D20', 'affirm_D21',
                'affirm_D22', 'affirm_D23', 'affirm_D24', 'affirm_D25', 'affirm_D26', 'affirm_D27', 'affirm_D28', 'affirm_D29', 'affirm_D30', 'affirm_D31', 'affirm_D32', 'affirm_D33', 'affirm_D34', 'affirm_D35', 'affirm_D36', 'affirm_D37', 'affirm_D38', 'affirm_D39', 'affirm_D40', 'affirm_D41', 'affirm_D42']
affirm_end = ['you would be inspired by <REPLACE>', 'you would feel your life was more meaningful because of <REPLACE>', 'you would feel fulfilled by <REPLACE>', 'you would feel grateful for your <REPLACE>', 'you would feel lucky to have your <REPLACE>', 'you would express thankfulness for your <REPLACE>', 'you would feel peaceful because of your <REPLACE>', 'you would feel empowered by your <REPLACE>', 'you would feel encouraged by your <REPLACE>', 'you would feel energized by your <REPLACE>', 'you would learn more about <REPLACE>', 'you would increase the amount of focus on <REPLACE> in your life', 'you would become a better person because of <REPLACE> in your life', 'your understanding of <REPLACE> would give you advantages in life', 'you would demonstrate your commitment to your <REPLACE>', 'your <REPLACE> would help you solve problems', 'you would feel that your <REPLACE> was an important part of who you are',
              'you would notice the positive impact of your <REPLACE> on your life', 'you would notice you had more <REPLACE> in your life', 'you would gain new appreciation for <REPLACE>', 'you would talk to others about your feelings about <REPLACE>', 'you would spend time with people who also value <REPLACE>', 'you would tell someone about your experiences with <REPLACE>', 'you would feel that your value of <REPLACE> was understood by others', 'you would feel you belong because you share a value of <REPLACE> with a group', 'others would look to you to learn about <REPLACE>', 'others would admire your <REPLACE>', 'your <REPLACE> would connect you with other people', 'your <REPLACE> would help you contribute to your community', 'you would be recognized for your <REPLACE>', 'you would be proud of your <REPLACE>', 'you would feel more free because of your <REPLACE>', 'you would feel motivated by your <REPLACE>', 
              'your <REPLACE> would give you a sense of purpose in life', 'your <REPLACE> would make you see the world in a more positive light', 'you would enjoy your <REPLACE>', 'your commitment to your <REPLACE> would make you feel like a valuable person', 'you would be safer because of your <REPLACE>', 'you would be happy because of your <REPLACE>', 'you would feel important because of your <REPLACE>', 'you would deal with sadness better because of your <REPLACE>']


mem_array = ['mem_D1', 'mem_D2', 'mem_D3', 'mem_D4', 'mem_D5', 'mem_D6', 'mem_D7', 'mem_D8', 'mem_D9', 'mem_D10', 'mem_D11', 'mem_D12', 'mem_D13', 'mem_D14', 'mem_D15', 'mem_D16', 'mem_D17', 'mem_D18', 'mem_D19', 'mem_D20', 'mem_D21',
             'mem_D22', 'mem_D23', 'mem_D24', 'mem_D25', 'mem_D26', 'mem_D27', 'mem_D28', 'mem_D29', 'mem_D30', 'mem_D31', 'mem_D32', 'mem_D33', 'mem_D34', 'mem_D35', 'mem_D36', 'mem_D37', 'mem_D38', 'mem_D39', 'mem_D40', 'mem_D41', 'mem_D42']
health_pos_end = ['If you sit less, you are more likely to live longer. You will be able to enjoy the people and things you love.','Active people often have lower blood sugar. Having healthy blood sugar can protect your arteries.','If you spend time walking, your bones will grow stronger. Stronger bones will help you stay pain-free.','If you become more active, you are less likely to get cancer. This means you may live longer than if you were more inactive.',
'People who are very active are about half as likely to die from cancer than those who spend all of their time sitting.','If you become more active, it is easier to digest food. This means you are less likely to get colon cancer.','People who become active have less of the hormones that help cancer grow. This means you are less likely to develop cancer.','People who become more active have less inflammation. This lowers your risk of illness.','People who become more active are less likely to develop diabetes. This means that your life could be more free.',
'Walking can help prevent you from getting diabetes. This will protect you from complications from other illnesses as well.','Walking can improve your strength, coordination, and balance, which reduces your risk for falls.','Walking regularly decreases your risk of injury from falling.','If you become active, your balance may improve. This can make everyday accidents less likely.','People who walk regularly lower their risk of hip fracture. This can protect your way of life.',
'If you walk regularly, your joints will be healthier. You are likely to stay mobile and pain-free for longer.','Walking regularly can make your heart stronger and help your endurance.','Physically active people are at lower risk for heart disease. This means fewer pills and lower risk of sickness.','Walking strengthens your heart. This means if you get sick, you are more likely to have only mild symptoms.','If you are more physically active, you may have more energy to devote to the things you care about.',
'Walking regularly can cause better sleep. You may feel more rested and have better concentration.','If you spend enough time moving, it may be easier to fall and stay asleep.','People who are physically active sleep more deeply. This means nights are more restful.','Walking regularly can help you feel more awake during the day.','If you spend enough time moving, you may decrease your risk of anxiety.','Walking regularly can improve your mood. This means you could feel happy and calm more often.','Walking can reduce stress. This benefits your mental health and makes it easier to enjoy your life.',
'If you spend enough time moving, you can improve your cognitive health.','Walking regularly can help keep your memory strong. This means your mind could be more alert as you get older.','If you spend time walking, you can help protect the brain’s memory areas as you age.','Being physically active can make it easier to pay attention. You may feel sharper and more observant.','Walking regularly can make it easier for you to learn new things.','Being active can help prevent high blood pressure and make your health easier to manage.',
'People who walk regularly have a lower risk of stroke and heart attack.','Walking regularly strengthens your immune system. This can help you stay healthy.','Moving can decrease your risk for chronic diseases.','Walking regularly at a brisk pace can help you think more quickly.','An active lifestyle can improve your brain health, making you better at planning ahead.','If you spend more time moving, you could have better control over your emotions.',
'If you become more active it may be easier for you to control your cholesterol.','Getting active will strengthen your muscles. This can make it easier for you to go where you want.','Walking briskly strengthens your lungs and improves your breathing.','Being active helps preserve your immune system, keeping you healthy.']
health_neg_end = ['If you stay inactive, you are more likely to die early. You may miss out on the people and things you love.',
'Inactive people often have higher blood sugar. Having high blood sugar can hurt your arteries.',
'If you don’t walk enough, your bones will grow weaker. Weaker bones make you more likely to have pain.',
'If you keep being inactive, you are more likely to get cancer. This means you may die earlier than if you were more active.',
'People who spend all of their time sitting are almost twice as likely to die from cancer than those who are very active.',
'If you continue to be inactive, it is more difficult to digest food. This means you are more likely to get colon cancer.',
'People who are inactive have more of the hormones that help cancer grow. This means you are more likely to develop cancer.',
'People who are inactive have more inflammation. This puts you at risk for many illnesses.',
'People who are inactive are more likely to develop diabetes. This means your life could be more limited.',
'Sitting too much increases your risk for diabetes. This can lead to serious complications from other illnesses as well.',
'Sitting too much can worsen your strength, coordination, and balance, which increases your risk for falls.',
'Being inactive increases your risk of injury from falling.',
'If you remain inactive, your balance is likely to decline. This can make everyday accidents more likely.',
'People who do not walk enough increase their risk of hip fracture. This can endanger your way of life.',
'If you don’t walk enough, your joints will be less healthy. You are likely to lose mobility and have pain sooner.',
'Not walking enough can weaken your heart and lower your endurance.',
'Inactive people are at serious risk for heart disease. This means more pills and higher risk of sickness.',
'Sitting too much weakens your heart. This means if you get sick, you are more likely to have severe complications.',
'If you remain inactive, you may have less energy to devote to the things you care about.',
'Sitting too much can cause poor sleep quality. You may feel more tired and have worse concentration.',
'If you do not move enough, it may be harder to fall and stay asleep.',
'People who are physically inactive sleep less deeply. This means nights are less restful.',
'Not walking enough can cause you to be sleepy during the day.',
'If you spend too much time sitting, you may increase your risk of anxiety.',
'Not walking enough can worsen your mood. This means you could feel unhappy and down more often.',
'Sitting too much can increase stress. This damages your mental health and makes it more difficult to enjoy your life.',
'If you spend too much time sitting, your cognitive health may decline more with age.',
'Not walking enough can worsen memory problems. This means your mind could be less alert as you get older.',
'If you spend too much time sitting, it will endanger the brain’s memory areas as you age.',
'Being physically inactive can make it harder to pay attention. You may feel foggier and less observant.',
'Not moving enough can make it harder for you to learn new things.',
'Being inactive can cause high blood pressure and make your health harder to manage.',
'People who do not move enough have a higher risk of stroke and heart attack.',
'Being inactive weakens your immune system. This may make you more vulnerable to illnesses.',
'Sitting too much can increase your risk for chronic diseases',
'Spending too much time sitting can cause you to think more slowly.',
'An inactive lifestyle can harm your brain health, making you worse at planning ahead.',
'If you spend too much time sitting, you may have worse control over your emotions.',
'If you remain inactive it may be harder for you to control your cholesterol.',
'If you don’t move enough, your muscles will become weak. This can make it difficult for you to go where you want.',
'Not walking enough can put you at risk for illnesses that harm your lungs and breathing.',
'Being inactive causes your immune system to deteriorate, making you less healthy.']

conf_array = ['conf_D1', 'conf_D2', 'conf_D3', 'conf_D4', 'conf_D5', 'conf_D6', 'conf_D7', 'conf_D8', 'conf_D9', 'conf_D10', 'conf_D11', 'conf_D12', 'conf_D13', 'conf_D14', 'conf_D15', 'conf_D16', 'conf_D17', 'conf_D18', 'conf_D19', 'conf_D20', 'conf_D21',
              'conf_D22', 'conf_D23', 'conf_D24', 'conf_D25', 'conf_D26', 'conf_D27', 'conf_D28', 'conf_D29', 'conf_D30', 'conf_D31', 'conf_D32', 'conf_D33', 'conf_D34', 'conf_D35', 'conf_D36', 'conf_D37', 'conf_D38', 'conf_D39', 'conf_D40', 'conf_D41', 'conf_D42']

mood_array = ['mood_D1', 'mood_D2', 'mood_D3', 'mood_D4', 'mood_D5', 'mood_D6', 'mood_D7', 'mood_D8', 'mood_D9', 'mood_D10', 'mood_D11', 'mood_D12', 'mood_D13', 'mood_D14', 'mood_D15', 'mood_D16', 'mood_D17', 'mood_D18', 'mood_D19', 'mood_D20', 'mood_D21',
              'mood_D22', 'mood_D23', 'mood_D24', 'mood_D25', 'mood_D26', 'mood_D27', 'mood_D28', 'mood_D29', 'mood_D30', 'mood_D31', 'mood_D32', 'mood_D33', 'mood_D34', 'mood_D35', 'mood_D36', 'mood_D37', 'mood_D38', 'mood_D39', 'mood_D40', 'mood_D41', 'mood_D42']

help_array = ['help_D1', 'help_D2', 'help_D3', 'help_D4', 'help_D5', 'help_D6', 'help_D7', 'help_D8', 'help_D9', 'help_D10', 'help_D11', 'help_D12', 'help_D13', 'help_D14', 'help_D15', 'help_D16', 'help_D17', 'help_D18', 'help_D19', 'help_D20', 'help_D21', 
              'help_D22', 'help_D23', 'help_D24', 'help_D25', 'help_D26', 'help_D27', 'help_D28', 'help_D29', 'help_D30', 'help_D31', 'help_D32', 'help_D33', 'help_D34', 'help_D35', 'help_D36', 'help_D37', 'help_D38', 'help_D39', 'help_D40', 'help_D41', 'help_D42']

tip_array = ['Walk to music with a beat to improve your walking speed and rhythm.',
'Breathe in rhythm to your walking.',
'Walk free: don’t take too much with you when you walk, and keep your hands free.',
'Keep a walking diary to track your progress.',
'Don’t just “think” your walking goals, write them down.',
'Walk at an intensity that you can talk but not sing.',
'Choose shoes with flat, supportive, flexible soles when you walk.',
'Don’t ignore pain or discomfort in your feet! Take care of them.',
'Walking is a dynamic exercise for the whole body: swing your arms when you walk.',
'Walk heel-to-toe: heel first, then push off with your toes.',
'Develop a good walking pattern. Having good form is most important.',
'Too busy for fitness? Try doing something active for just 5 minutes instead. It adds up.',
'Create a routine to fit physical activity into your schedule. For example, you could walk after lunch every day.',
'Set short-term goals, like taking the stairs every day for one week. You will feel a sense of accomplishment more quickly.',
'Schedule your time to be physically active a few days in advance.',
'Try lots of different activities, or go for walks in different places. This will help you stay interested.',
'Reward yourself for exercising. For example, after a brisk walk, enjoy a cup of coffee or your favorite show.',
'Plan fun activities at convenient times of day. This will make it easier to stick with your plans.',
'Try replacing some TV or computer time with a walk.',
'Think of nearby places you go to often. Try walking to these places instead of driving.',
'Give yourself reminders to get active. You could leave shoes next to your bed so you remember to go for a walk every morning.',
'Walking is one of the most meaningful activities you can do: go out and explore new neighborhoods.',
'Make a list of places of interest near your home. Walk to them whenever you have some extra time on your hands.',
'Pay attention to how your body feels when you go for walks. This will increase the benefits of activity and prevent injury.',
'Listen to music, an audiobook, or a podcast while you walk.',
'You can combine other hobbies with physical activity. If you like photography, you could bring your camera on a nature hike.',
'Make sure to praise yourself even for small accomplishments, like going through with a planned morning walk.',
'Don’t walk around aimlessly. Have a plan and a destination.',
'Set a specific goal: walk 5 minutes at an even pace.',
'Set an ultimate goal for 20 to 30 minutes of continuous walking every day, but start small.',
'The best parking spots for your health are farther away. Choose the last row of a parking lot or the top floor so that you have further to walk.',
'Try sweeping, vacuuming, or doing yard work just a little more rigorously to get your heart rate up.',
'Set a timer so you don’t sit for more than 30 minutes at a time.',
'Do something active around the house during commercial breaks.',
'Instead of sitting down to talk on the phone, pace around your home.',
'Ask others what they do to get active, and see if you can get any good ideas from them.',
'Create fitness goals with other people and help each other stick to them.',
'Tell others about your movement goals to stay accountable.',
'Get other people in your household to join you in getting active around your home. If you live alone, call a friend to include them.',
'Put on some music while you do housework and move to the beat. Dance around to music while you tidy, do dishes, or dust.',
'Marching in place or taking laps around your home can feel silly, but it is healthy. Have fun with it.',
'If you have access to stairs, try walking up and down them for no reason every once in a while.']



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

    FROM = "dashstudy2021@gmail.com"

    TO = ["frankdag20@gmail.com"]  # must be a list

    SUBJECT = "Hello!"
    TEXT = f"Hello, Participant {participant} has requested that someone reach out to them for assistance."

    message = """Subject: %s

    %s
     """ % (f"DASH: Participant {participant} is requesting assistance.", TEXT)

    # Send the mail
    username = str("dashstudy2021@gmail.com")
    password = str("bhFw3mL$mR")

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
    form_fields = ['posOrNeg', 'affirmVal', 'day_track']

    def is_displayed(self):

        return self.get_timeout_seconds() != 0

########################################

class Intro_all(Page):
    form_model = 'player'

    track_day = 0
    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        y = fix_time(y)
        check_notif_time(y)

        return (self.participant.vars['expiry'] - int(y)-8) * 3600

    def before_next_page(self):
        self.participant.vars['expiry'] = int("29")

        track_day = self.player.daysurv
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

class MyPage_all(Page):
    form_model = 'player'

    def get_form_fields(self):

        return affirm_array[self.player.day_track-1],

    def vars_for_template(self):

        affirm_value = self.player.affirmVal
        insert_word_affirm = affirm_end[self.player.day_track-1].replace('<REPLACE>', affirm_value)
        return dict(
            end_of_q = insert_word_affirm,
        )

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        y = fix_time(y)
        check_notif_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class MyPage2_all(Page):
    form_model = 'player'

    def get_form_fields(self):

        return conf_array[self.player.day_track-1], 'checkslider',

    def checkslider_error_message(self, value):
            if not value:
                return 'Please make your decision using slider.'

    def vars_for_template(self):
        return dict(
            tip = tip_array[self.player.day_track-1],
            conf_day_name = conf_array[self.player.day_track-1],
        )

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class MyPage3_all(Page):
    form_model = 'player'

    def vars_for_template(self):
        health_message = self.player.posOrNeg

        self.player.seen_or_not = 1

        if health_message == False:
            disp = health_pos_end[self.player.day_track-1]
        if health_message == True:
            disp = health_neg_end[self.player.day_track-1]

        return dict(
            disp_health_message=disp,
        )

    def get_form_fields(self):

        return mem_array[self.player.day_track-1],

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class MyPage4_all(Page):
    form_model = 'player'
    def get_form_fields(self):

        return mood_array[self.player.day_track-1],

    def js_vars(self):
        return dict(
            mood_day=mood_array[self.player.day_track-1],
        )

    def vars_for_template(self):
         return dict(
            mood_day=mood_array[self.player.day_track-1],
        )

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class MyPage5_all(Page):
    form_model = 'player'

    def get_form_fields(self):

        return help_array[self.player.day_track-1],

    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        check_notif_time(y)
        y = fix_time(y)
        return (self.participant.vars['expiry'] - int(y)) * 3600

    def is_displayed(self):
        return self.get_timeout_seconds() != 0

class Wait_all(Page):
    form_model = 'player'


    def vars_for_template(self):

        self_help_array = [self.player.help_D1, self.player.help_D2, self.player.help_D3, self.player.help_D4, self.player.help_D5, self.player.help_D6, self.player.help_D7, self.player.help_D8, self.player.help_D9, self.player.help_D10, self.player.help_D11, self.player.help_D12, self.player.help_D13,
                   self.player.help_D14, self.player.help_D15, self.player.help_D16, self.player.help_D17, self.player.help_D18, self.player.help_D19, self.player.help_D20, self.player.help_D21, self.player.help_D22, self.player.help_D23, self.player.help_D24, self.player.help_D25,self.player.help_D26,
                   self.player.help_D27, self.player.help_D28, self.player.help_D29, self.player.help_D30, self.player.help_D31, self.player.help_D32, self.player.help_D33, self.player.help_D34, self.player.help_D35,
                   self.player.help_D36, self.player.help_D37, self.player.help_D38, self.player.help_D39, self.player.help_D40, self.player.help_D41, self.player.help_D42]


        assist = self_help_array[self.player.day_track-1]
        if assist == True:
            send_email_help(self.player.id_in_group)

    def before_next_page(self):
        from datetime import datetime

        self.player.day_track = self.player.day_track + 1

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

class Intro_D1(Page):
    form_model = 'player'

    track_day = 0
    def get_timeout_seconds(self):
        x = datetime.now()
        y = x.strftime("%H")

        y = fix_time(y)
        check_notif_time(y)

        return (self.participant.vars['expiry'] - int(y)-8) * 3600

    def before_next_page(self):
        self.participant.vars['expiry'] = int("29")

        track_day = self.player.daysurv
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

    def get_form_fields(self):
        if self.player.daysurv == 2:
            return ['affirm_D1']
        else:
            return ['affirm_D2']

    def vars_for_template(self):

        affirm_value = self.player.affirmVal
        return dict(
            end_of_q = "you would be inspired by",
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

    form_fields = ['mem_D1']

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
    form_fields = ['conf_D1', 'checkslider']


    def vars_for_template(self):
        return dict(
            tip="Walk to music with a beat to improve your walking speed and rhythm."
        )

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

        self.player.daysurv += 1
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
        self.player.time_begin_d5 = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
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
    #form_fields = [page5[0]]

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
   # Intro_D3, MyPage_D3, MyPage2_D3, MyPage3_D3, MyPage4_D3, MyPage5_D3, Wait_D3,
    # Intro_D4, MyPage_D4, MyPage2_D4, MyPage3_D4, MyPage4_D4, MyPage5_D4, Wait_D4,
    # Intro_D5, MyPage_D5, MyPage2_D5, MyPage3_D5, MyPage4_D5, MyPage5_D5, Wait_D5,
    # Intro_D6, MyPage_D6, MyPage2_D6, MyPage3_D6, MyPage4_D6, MyPage5_D6, Wait_D6,
page_sequence = [PreTrial, Start, Intro_all, MyPage_all, MyPage2_all, MyPage3_all, MyPage4_all, MyPage5_all, Wait_all]
                 #Start, Intro_D1, MyPage_D1, MyPage3_D1, MyPage2_D1, MyPage4_D1, MyPage5_D1, Wait_D1
                # ]
