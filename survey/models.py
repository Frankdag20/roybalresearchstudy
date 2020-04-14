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


class Player(BasePlayer):

    value = models.StringField(
        choices=[["family", "family"],["money","money"],["religion","religion"]],
        label="Please select the designated value of importance for the participant.",
        widget=widgets.RadioSelect)

    Page1affirm = models.BooleanField(
        choices=[[True, 'Please spend 30 seconds visualizing that time in as much detail as possible, then press this button.']],
        label='Think of a time when you would be inspired by %s' % self.value,
        widget=widgets.RadioSelect)
    Page2healthM = models.BooleanField(
        choices=[[True,'Please press this button when finished reading.']],
        label='As you move around more, your body can use blood sugar. This can keep your arteries healthy.',
        widget=widgets.RadioSelect)
    Page3healthT = models.BooleanField(
        choices=[["1", '1'], ["2", '2'], ["3", '3'], ["4", '4'], ["5", '5'], ["6", '6']],
        label='How likely are you to try this health tip?',
        widget=widgets.RadioSelectHorizontal)
    Page5mood = models.StringField(
        choices=[["1", '😄'], ["2", '🙂'], ["3", '😐'], ["4", '🙁'], ["5", '😧']],
        label='What is your current mood? Please rank from happy (smiley face) to negative (sad face).',
        widget=widgets.RadioSelectHorizontal)
    affirm1 = models.BooleanField(
        choices=[[True, 'Press when you have thought of the situation.']],
        label='Imagine a time when you would have fun with your family and friends.',
        widget=widgets.RadioSelect)
    affirm2 = models.BooleanField(
        choices=[[True, 'Press when you have thought of the situation.']],
        label='Imagine a time when you would be inspired by creativity.',
        widget=widgets.RadioSelect)
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
