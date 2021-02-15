from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import survey.sendEmail
import csv
from datetime import datetime
import time
import calendar

author = 'Frank DAgostino'

doc = """
Roybal Research study program to sent daily survey
to participates to test affirmation messaging research.
See dailyQs.csv for input data
"""


class Constants(BaseConstants):
    name_in_url = 'research'
    players_per_group = None

    num_rounds = 1


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    checkslider = models.IntegerField(blank=True)
    def checkslider_error_message(self, value):
        if not value:
            return 'Please make your decision using the slider.'

    val_label = models.StringField()
    affirm_question = models.StringField()

    seen_or_not = models.BooleanField()

    def check_correct(self):
        if ((self.submitted_answer == "I am confident that I have seen this message in the scanner before.") and (self.seen_or_not == 1)):
            self.is_correct = "Hit"
            return
        elif ((self.submitted_answer == "I can confidently say I've never seen this message in the scanner before.") and (self.seen_or_not == 1)):
            self.is_correct = "Miss"
            return
        elif ((self.submitted_answer == "I am confident that I have seen this message in the scanner before.") and (self.seen_or_not == 0)):
            self.is_correct = "False Alarm"
            return
        elif ((self.submitted_answer == "I can confidently say I've never seen this message in the scanner before.") and (self.seen_or_not == 0)):
            self.is_correct = "Correct Rejection"
            return
        elif ((self.submitted_answer == "This message seems vaguely familiar, but I am not confident.") and (self.seen_or_not == 1)):
            self.is_correct = "Unsure Hit"
            return
        elif ((self.submitted_answer == "This message does not seem familiar, although I am not confident.") and (self.seen_or_not == 1)):
            self.is_correct = "Unsure Miss"
            return
        elif ((self.submitted_answer == "This message seems vaguely familiar, but I am not confident.") and (self.seen_or_not == 0)):
            self.is_correct = "Unsure False Alarm"
            return
        elif ((self.submitted_answer == "This message does not seem familiar, although I am not confident.") and (self.seen_or_not == 0)):
            self.is_correct = "Unsure Correct Rejection"
            return

    daysurv = models.IntegerField(initial=1)

    day_track = models.IntegerField(initial=1)

    mood_temp = models.StringField(blank=True)

    track = models.IntegerField()

    posOrNeg = models.BooleanField(
        choices=[[True, 'Positive'], [False, 'Negative']],
        label='Please choose whether this participant will receive positive or negative health messages throughout the study.',
        widget=widgets.RadioSelectHorizontal)

    affirmVal = models.StringField(
        label='Please choose what value this participant deems most important to them.',
        widget=widgets.RadioSelectHorizontal, choices=[['family and friends', 'family and friends'], ['humor', 'humor'], ['spontaneity', 'spontaneity'], ['money', 'money'], ['religion', 'religion'], ['health', 'health'],  ['politics', 'politics'], ['independence', 'independence'], ['creativity', 'creativity']])

    ####################################################################33

    affirm_D1 = models.BooleanField(
        choices=[[True,'I visualized for 30 seconds.']],
        label='Press the following button to affirm you completed the task.',
        widget=widgets.RadioSelect)

    conf_D1 = models.IntegerField(

        label='Please choose your confidence level below.')
     
    mem_D1 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )

    mood_D1 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)

    help_D1 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)

    accel_D1 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Make sure you are wearing your accelerometer as often as possible this week! Have you been wearing your accelerometer?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D2 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)

    conf_D2 = models.IntegerField(

        label='Please choose your confidence level below.')

    mem_D2 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )

    mood_D2 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)

    help_D2 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)

    accel_D2 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Make sure you are wearing your accelerometer as often as possible this week! Have you been wearing your accelerometer?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D3 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D3 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D3 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    
    mood_D3 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D3 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)

    accel_D3 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Make sure you are wearing your accelerometer as often as possible this week! Have you been wearing your accelerometer?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D4 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D4 = models.IntegerField(

        label='Please choose your confidence level below.')
    
    mem_D4 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    mood_D4 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D4 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)

    accel_D4 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Make sure you are wearing your accelerometer as often as possible this week! Have you been wearing your accelerometer?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D5 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D5 = models.IntegerField(

        label='Please choose your confidence level below.')
    
    mem_D5 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    mood_D5 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D5 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)

    accel_D5 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Make sure you are wearing your accelerometer as often as possible this week! Have you been wearing your accelerometer?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D6 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D6 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D6 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    
    mood_D6 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D6 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)

    accel_D6 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Make sure you are wearing your accelerometer as often as possible this week! Have you been wearing your accelerometer?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D7 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D7 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D7 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    
    mood_D7 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D7 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)

    accel_D7 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Make sure you are wearing your accelerometer as often as possible this week! Have you been wearing your accelerometer?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D8 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D8 = models.IntegerField(

        label='Please choose your confidence level below.')
    
    mem_D8 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    mood_D8 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D8 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D9 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)

    conf_D9 = models.IntegerField(

        label='Please choose your confidence level below.')
    
    mem_D9 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    mood_D9 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D9 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D10 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D10 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D10 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    
    mood_D10 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D10 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D11 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D11 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D11 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    
    mood_D11 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D11 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D12 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D12 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D12 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    
    mood_D12 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D12 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D13 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D13 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D13 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    
    mood_D13 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D13 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D14 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D14 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D14 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    
    mood_D14 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D14 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D15 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D15 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D15 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    
    mood_D15 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D15 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    accel_D15 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Make sure you are wearing your accelerometer as often as possible this week! Have you been wearing your accelerometer?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D16 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D16 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D16 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    
    mood_D16 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D16 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    accel_D16 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Make sure you are wearing your accelerometer as often as possible this week! Have you been wearing your accelerometer?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D17 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D17 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D17 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    
    mood_D17 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D17 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    accel_D17 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Make sure you are wearing your accelerometer as often as possible this week! Have you been wearing your accelerometer?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D18 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D18 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D18 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    
    mood_D18 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D18 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    accel_D18 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Make sure you are wearing your accelerometer as often as possible this week! Have you been wearing your accelerometer?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D19 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D19 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D19 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    
    mood_D19 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D19 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    accel_D19 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Make sure you are wearing your accelerometer as often as possible this week! Have you been wearing your accelerometer?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D20 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D20 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D20 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    
    mood_D20 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D20 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    accel_D20 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Make sure you are wearing your accelerometer as often as possible this week! Have you been wearing your accelerometer?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D21 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D21 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D21 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    
    mood_D21 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D21 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    accel_D21 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Make sure you are wearing your accelerometer as often as possible this week! Have you been wearing your accelerometer?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D22 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D22 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D22 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    
    mood_D22 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D22 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D23 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D23 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D23 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    
    mood_D23 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D23 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D24 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D24 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D24 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    mood_D24 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D24 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D25 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D25 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D25 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    mood_D25 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D25 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D26 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D26 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D26 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    mood_D26 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D26 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D27 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D27 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D27 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    mood_D27 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D27 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D28 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D28 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D28 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    mood_D28 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D28 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D29 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D29 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D29 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    mood_D29 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D29 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D30 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D30 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D30 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    mood_D30 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D30 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D31 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D31 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D31 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    mood_D31 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D31 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D32 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D32 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D32 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    mood_D32 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D32 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D33 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D33 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D33 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    mood_D33 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D33 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D34 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D34 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D34 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    mood_D34 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D34 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D35 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D35 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D35 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    mood_D35 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D35 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D36 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D36 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D36 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    mood_D36 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D36 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    accel_D36 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Make sure you are wearing your accelerometer as often as possible this week! Have you been wearing your accelerometer?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D37 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D37 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D37 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    mood_D37 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D37 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    accel_D37 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Make sure you are wearing your accelerometer as often as possible this week! Have you been wearing your accelerometer?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D38 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D38 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D38 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    mood_D38 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D38 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    accel_D38 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Make sure you are wearing your accelerometer as often as possible this week! Have you been wearing your accelerometer?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D39 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D39 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D39 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    mood_D39 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D39 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    accel_D39 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Make sure you are wearing your accelerometer as often as possible this week! Have you been wearing your accelerometer?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D40 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D40 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D40 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    mood_D40 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D40 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    accel_D40 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Make sure you are wearing your accelerometer as often as possible this week! Have you been wearing your accelerometer?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D41 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D41 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D41 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    mood_D41 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D41 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    accel_D41 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Make sure you are wearing your accelerometer as often as possible this week! Have you been wearing your accelerometer?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D42 = models.BooleanField(
        choices=[[True, 'I visualized for 30 seconds.']],
        label="Press the following button to affirm you completed the task.",
        widget=widgets.RadioSelect)
    conf_D42 = models.IntegerField(

        label='Please choose your confidence level below.')
    mem_D42 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before in the scanner?",
        widget=widgets.RadioSelect
    )
    mood_D42 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How do you rate your mood for today?',
        widget=widgets.RadioSelect)
    help_D42 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    accel_D42 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Make sure you are wearing your accelerometer as often as possible this week! Have you been wearing your accelerometer?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    time_begin_D1 = models.StringField()
    time_begin_D2 = models.StringField()
    time_begin_D3 = models.StringField()
    time_begin_D4 = models.StringField()
    time_begin_D5 = models.StringField()
    time_begin_D6 = models.StringField()
    time_begin_D7 = models.StringField()
    time_begin_D8 = models.StringField()
    time_begin_D9 = models.StringField()
    time_begin_D10 = models.StringField()
    time_begin_D11 = models.StringField()
    time_begin_D12 = models.StringField()
    time_begin_D13 = models.StringField()
    time_begin_D14 = models.StringField()
    time_begin_D15 = models.StringField()
    time_begin_D16 = models.StringField()
    time_begin_D17 = models.StringField()
    time_begin_D18 = models.StringField()
    time_begin_D19 = models.StringField()
    time_begin_D20 = models.StringField()
    time_begin_D21 = models.StringField()
    time_begin_D22 = models.StringField()
    time_begin_D23 = models.StringField()
    time_begin_D24 = models.StringField()
    time_begin_D25 = models.StringField()
    time_begin_D26 = models.StringField()
    time_begin_D27 = models.StringField()
    time_begin_D28 = models.StringField()
    time_begin_D29 = models.StringField()
    time_begin_D30 = models.StringField()
    time_begin_D31 = models.StringField()
    time_begin_D32 = models.StringField()
    time_begin_D33 = models.StringField()
    time_begin_D34 = models.StringField()
    time_begin_D35 = models.StringField()
    time_begin_D36 = models.StringField()
    time_begin_D37 = models.StringField()
    time_begin_D38 = models.StringField()
    time_begin_D39 = models.StringField()
    time_begin_D40 = models.StringField()
    time_begin_D41 = models.StringField()
    time_begin_D42 = models.StringField()