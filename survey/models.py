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


author = 'Frank DAgostino'

doc = """
Research
"""


class Constants(BaseConstants):
    name_in_url = 'research'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

# def insert_val(val):
#     return models.BooleanField(
#         choices=[[True, 'Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.']],
#         label= val,
#         widget=widgets.RadioSelect)

class Player(BasePlayer):

    valueP1 = models.StringField(
        choices=[["Think of a time when you would be inspired by family, and focus on the thoughts and emotions associated with the experience.", "family"],
                 ["Think of a time when you would be inspired by money, and focus on the thoughts and emotions associated with the experience.","money"],
                 ["Think of a time when you would be inspired by religion, and focus on the thoughts and emotions associated with the experience.","religion"]],
        label="Please select the designated value of importance for the participant.",
        widget=widgets.RadioSelect)
    valueP2 = models.StringField(
        choices=[["As you move around more in your day-to-day life, your body can use blood sugar. This can keep your arteries healthy. Have you seen this message while in the MRI scanner before?", "positive"],
                 ["If you do not move around more in your day-to-day life, your body does not use blood sugar. This can make your arteries unhealthy. Have you seen this message while in the MRI scanner before?","negative"]],
        label="Please select whether the participant should have a positive or negative health tip.",
        widget=widgets.RadioSelect)

    Page1affirm = models.BooleanField(
         choices=[[True, 'Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.']],
         label="----",
         widget=widgets.RadioSelect)

    Page2healthM = models.StringField(
        choices=[["CO", "I am confident that I have seen this message in the scanner before."],
                 ["CN", "I can confidently say I've never seen this message in the scanner before."],
                 ["UO", "This message seems vaguely familiar, but I am not confident."],
                 ["UN", "This message does not seem familiar, although I am not confident"]],
        label="----",
        widget=widgets.RadioSelect)
    Page3healthT = models.StringField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How confident are you in carrying out the previous health tip?',
        widget=widgets.RadioSelectHorizontal)
    Page4mood = models.StringField(
        choices=[["1", '😄'], ["2", '🙂'], ["3", '😐'], ["4", '🙁'], ["5", '😧']],
        label='What is your current mood? Please rank from happy (smiley face) to negative (sad face).',
        widget=widgets.RadioSelectHorizontal)
    accel = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Make sure you are wearing your accelerometer as often as possible this week! Have you been wearing your accelerometer?',
        widget=widgets.RadioSelectHorizontal)
    help = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Please feel welcome to reach out with any questions or concerns you may have. Would you want a research coordinator to reach out to you?',
        widget=widgets.RadioSelectHorizontal)

    affirm3 = models.BooleanField(
        choices=[[True, 'Press when you have thought of the situation.']],
        label='Imagine a time when you would feel grateful for your independence.',
        widget=widgets.RadioSelect)
    healthP1 = models.BooleanField(
        choices=[[True, 'Press when you have read the following statement.']],
        label='If you start to sit less, you are more likely to live longer. You will be able to enjoy the people and things you love.',
        widget=widgets.RadioSelect)
    healthP2 = models.BooleanField(
        choices=[[True, 'Press when you have read the following statement.']],
        label='As you move around more, your body can use blood sugar. This can keep your arteries healthy.',
        widget=widgets.RadioSelect)
    healthP3 = models.BooleanField(
        choices=[[True, 'Press when you have read the following statement.']],
        label='If you become less sedentary, your bones will stay stronger as you get older. This makes it easier to do things you like.',
        widget=widgets.RadioSelect)
    healthN1 = models.BooleanField(
        choices=[[True, 'Press when you have read the following statement.']],
        label='If you stay inactive, you are more likely to die early. You may miss out on the people and things you love.',
        widget=widgets.RadioSelect)
    healthN2 = models.BooleanField(
        choices=[[True, 'Press when you have read the following statement.']],
        label='As you move around less, your body cannot use blood sugar. This can make your arteries sick.',
        widget=widgets.RadioSelect)
    healthN3 = models.BooleanField(
        choices=[[True, 'Press when you have read the following statement.']],
        label='If you continue to be sedentary, your bones will weaken faster as you get older. This makes it harder to do things you like.',
        widget=widgets.RadioSelect)
    healthT1 = models.BooleanField(
        choices=[[True, 'Press when you have read the following statement.']],
        label='Think of nearby places you go often. Try walking to these places instead of driving.',
        widget=widgets.RadioSelect)
    healthT2 = models.BooleanField(
        choices=[[True, 'Press when you have read the following statement.']],
        label='Find a time every day when you can get out and walk around for at least 15 minutes. For example, maybe you can walk to and from the grocery store every day.',
        widget=widgets.RadioSelect)
    healthT3 = models.BooleanField(
        choices=[[True, 'Press when you have read the following statement.']],
        label='Make a habit of walking up and down the stairs whenever you can. Avoid taking the elevator as often as possible.',
        widget=widgets.RadioSelect)
    healthtip = models.BooleanField(
        choices=[[True, 'How likely are you to try this health tip?']],
        label='How likely are you to try this health tip?',
        widget=widgets.RadioSelect)
    #info2 = models.BooleanField(
    #    choices=[[True, 'New Statement'], [False, 'Old Statement']],
    #    label='You are more likely to live longer and enjoy people and things you love if you start to sit less.',
    #    widget=widgets.RadioSelectHorizontal)
    # info3 = models.StringField(
    #     choices=[[1, 'Unlikely \n 1'], ['2', '2'], ['3', 'Neutral \n 3'], ['4', '4'], ['5', 'Very Likely \n 5']],
    #     label='Think of nearby places you go often. Try walking to these places instead of driving. How likely are you to do this in your daily life? (1 unlikely - 5 very likely)',
    #     widget=widgets.RadioSelectHorizontal)
    info3 = models.IntegerField(
        label='Think of nearby places you go often. Try walking to these places instead of driving. How likely are you to do this in your daily life?',
        widget=widgets.RadioSelectHorizontal, choices=[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]])
    info4 = models.StringField(
        choices=[['1', '😄'], ['2', '🙂'], ['3', '😐'], ['4', '🙁'], ['5', '😧']],
        label='Mood?',
        widget=widgets.RadioSelectHorizontal)
    # info5 = models.StringField(
    #     label='What time did you get into bed last night?')
    # info6 = models.StringField(
    #     label='What time did you go to sleep last night?')
    # info7 = models.StringField(
    #     label='What time did you wake up?')
    # info8 = models.StringField(
    #     label='What time did you get out of bed?')
    # info9 = models.BooleanField(
    #     choices=[[True, 'Yes'], [False, 'No']],
    #     label='Did you remove any of the monitors for >10 minutes today?',
    #     widget=widgets.RadioSelectHorizontal)
