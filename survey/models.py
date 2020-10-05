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

    with open('survey/dailyQs.csv') as questions_file:
        questions = list(csv.DictReader(questions_file))

    with open('survey/affirmQs.csv') as aff:
        affirm_file = list(csv.DictReader(aff))

    with open('survey/values.csv') as val:
        val_file = list(csv.DictReader(val))

    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:

            self.session.vars['questions'] = Constants.questions.copy()
            self.session.vars['affirm_file'] = Constants.affirm_file.copy()
            self.session.vars['val_file'] = Constants.val_file.copy()
            # randomize for each participant
            # import random
            # randomized_questions = random.sample(Constants.questions, len(Constants.questions))
            # self.participant.vars['questions'] = randomized_questions

        for p in self.get_players():
            question_data = p.current_question()
            p.question_id = int(question_data['id'])
            p.question = question_data['question']
            p.solution = question_data['solution']
            p.seen = int(question_data['seen'])

            data = p.current_question_affirm()
            p.val_label = p.get_value()
            p.affirm_question = data[p.val_label]


class Group(BaseGroup):
    pass

class Player(BasePlayer):

    question_id = models.IntegerField()
    seen = models.IntegerField()
    question = models.StringField()
    solution = models.StringField()
    submitted_answer = models.StringField(widget=widgets.RadioSelect)
    is_correct = models.StringField()

    val_label = models.StringField()
    affirm_question = models.StringField()

    seen_or_not = models.BooleanField()

    def get_value(self):
        return self.session.vars['val_file'][0]['value']

    def current_question(self):
        return self.session.vars['questions'][self.daysurv]

    def current_question_affirm(self):
        return self.session.vars['affirm_file'][self.daysurv]

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

    time_begin_d1 = models.StringField()
    time_begin_d2 = models.StringField()
    time_begin_d3 = models.StringField()
    time_begin_d4 = models.StringField()
    time_begin_d5 = models.StringField()
    time_begin_d6 = models.StringField()
    time_begin_d7 = models.StringField()
    time_begin_d8 = models.StringField()
    time_begin_d9 = models.StringField()
    time_begin_d10 = models.StringField()
    time_begin_d11 = models.StringField()
    time_begin_d12 = models.StringField()
    time_begin_d13 = models.StringField()
    time_begin_d14 = models.StringField()
    time_begin_d15 = models.StringField()
    time_begin_d16 = models.StringField()
    time_begin_d17 = models.StringField()
    time_begin_d18 = models.StringField()
    time_begin_d19 = models.StringField()
    time_begin_d20 = models.StringField()
    time_begin_d21 = models.StringField()
    time_begin_d22 = models.StringField()
    time_begin_d23 = models.StringField()
    time_begin_d24 = models.StringField()
    time_begin_d25 = models.StringField()
    time_begin_d26 = models.StringField()
    time_begin_d27 = models.StringField()
    time_begin_d28 = models.StringField()
    time_begin_d29 = models.StringField()
    time_begin_d30 = models.StringField()
    time_begin_d31 = models.StringField()
    time_begin_d32 = models.StringField()
    time_begin_d33 = models.StringField()
    time_begin_d34 = models.StringField()
    time_begin_d35 = models.StringField()
    time_begin_d36 = models.StringField()
    time_begin_d37 = models.StringField()
    time_begin_d38 = models.StringField()
    time_begin_d39 = models.StringField()
    time_begin_d40 = models.StringField()
    time_begin_d41 = models.StringField()
    time_begin_d42 = models.StringField()


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
        label='Press the following button to affirm you completed the task',
        widget=widgets.RadioSelect)

    conf_D1 = models.IntegerField(
        #choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"], ["4", "Confident I've seen it before"]],

        label='Please choose your confidence level below')

    mem_D1 = models.StringField(
        choices=[["1", "Confident it's new"], ["2", "Unconfident it's new"], ["3", "Unconfident I've seen it before"],
                 ["4", "Confident I've seen it before"]],
        label = "How confident are you that you've seen this message before?"
        widget = widgets.RadioSelect
    )

    mood_D1 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
        widget=widgets.RadioSelect)

    help_D1 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)

    ####################################################################33

    affirm_D2 = models.BooleanField(
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)

    conf_D2 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)

    mood_D2 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
        widget=widgets.RadioSelect)

    help_D2 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)

    ####################################################################33

    affirm_D3 = models.BooleanField(
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D3 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D3 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
        widget=widgets.RadioSelect)
    help_D3 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)

    ####################################################################33

    affirm_D4 = models.BooleanField(
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D4 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D4 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
        widget=widgets.RadioSelect)
    help_D4 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D5 = models.BooleanField(
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D5 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D5 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
        widget=widgets.RadioSelect)
    help_D5 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D6 = models.BooleanField(
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D6 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D6 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
        widget=widgets.RadioSelect)
    help_D6 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D7 = models.BooleanField(
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D7 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D7 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
        widget=widgets.RadioSelect)
    help_D7 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D8 = models.BooleanField(
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D8 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D8 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
        widget=widgets.RadioSelect)
    help_D8 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D9 = models.BooleanField(
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)

    conf_D9 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D9 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
        widget=widgets.RadioSelect)
    help_D9 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D10 = models.BooleanField(
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D10 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D10 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
        widget=widgets.RadioSelect)
    help_D10 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D11 = models.BooleanField(
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D11 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D11 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
        widget=widgets.RadioSelect)
    help_D11 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D12 = models.BooleanField(
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D12 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D12 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
        widget=widgets.RadioSelect)
    help_D12 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D13 = models.BooleanField(
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D13 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D13 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
        widget=widgets.RadioSelect)
    help_D13 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D14 = models.BooleanField(
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D14 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D14 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
        widget=widgets.RadioSelect)
    help_D14 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D15 = models.BooleanField(
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D15 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D15 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
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
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D16 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D16 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
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
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D17 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D17 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
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
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D18 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D18 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
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
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D19 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D19 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
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
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D20 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D20 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
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
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D21 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D21 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
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
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D22 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D22 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
        widget=widgets.RadioSelect)
    help_D22 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D23 = models.BooleanField(
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D23 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D23 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
        widget=widgets.RadioSelect)
    help_D23 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D24 = models.BooleanField(
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D24 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D24 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
        widget=widgets.RadioSelect)
    help_D24 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D25 = models.BooleanField(
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D25 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D25 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
        widget=widgets.RadioSelect)
    help_D25 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D26 = models.BooleanField(
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D26 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D26 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
        widget=widgets.RadioSelect)
    help_D26 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D27 = models.BooleanField(
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D27 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D27 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
        widget=widgets.RadioSelect)
    help_D27 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D28 = models.BooleanField(
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D28 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D28 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
        widget=widgets.RadioSelect)
    help_D28 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D29 = models.BooleanField(
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D29 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D29 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
        widget=widgets.RadioSelect)
    help_D29 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D30 = models.BooleanField(
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D30 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D30 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
        widget=widgets.RadioSelect)
    help_D30 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D31 = models.BooleanField(
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D31 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D31 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
        widget=widgets.RadioSelect)
    help_D31 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D32 = models.BooleanField(
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D32 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D32 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
        widget=widgets.RadioSelect)
    help_D32 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D33 = models.BooleanField(
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D33 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D33 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
        widget=widgets.RadioSelect)
    help_D33 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D34 = models.BooleanField(
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D34 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D34 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
        widget=widgets.RadioSelect)
    help_D34 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D35 = models.BooleanField(
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D35 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D35 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
        widget=widgets.RadioSelect)
    help_D35 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D36 = models.BooleanField(
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D36 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D36 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
        widget=widgets.RadioSelect)
    help_D36 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)
    ####################################################################33

    affirm_D37 = models.BooleanField(
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D37 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D37 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
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
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D38 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D38 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
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
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D39 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D39 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
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
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D40 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D40 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
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
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D41 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D41 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
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
        choices=[[True, 'Press this button when finished visualizing.']],
        label="Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.",
        widget=widgets.RadioSelect)
    conf_D42 = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip on a scale from 1 to 6?',
        widget=widgets.RadioSelectHorizontal)
    mood_D42 = models.StringField(
        choices=[["1", 'Very Bad'], ["2", 'Bad'], ["3", 'So-so'], ["4", 'Good'],
                 ["5", 'Very Good']],
        label='How are you feeling? Please rank from very bad to very good.',
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

