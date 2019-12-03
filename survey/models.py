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
    info1 = models.BooleanField(
        choices=[[True, 'Press when you have thought of a situation.']],
        label='Think of  a time in the future when you were inspired by family and friends.',
        widget=widgets.RadioSelect)
    info2 = models.BooleanField(
        choices=[[True, 'New'], [False, 'Old']],
        label='You are more likely to live longer and enjoy people and things you love if you start to sit less.',
        widget=widgets.RadioSelectHorizontal)
    info3 = models.IntegerField(
        choices=[[1, 'Unlikely \n 1'], ['2', '2'], ['3', 'Neutral \n 3'], ['4', '4'], ['5', 'Very Likely \n 5']],
        label='Think of nearby places you go often. Try walking to these places instead of driving. How likely are you to do this in your daily life? (1 unlikely - 5 very likely)',
        widget=widgets.RadioSelectHorizontal)
    info4 = models.IntegerField(
        choices=[['1', '😄'], ['2', '🙂'], ['3', '😐'], ['4', '🙁'], ['5', '😧']],
        label='Mood?',
        widget=widgets.RadioSelectHorizontal)
    info5 = models.TimeField(
        label='What time did you get into bed last night?')
    info6 = models.TimeField(
        label='What time did you go to sleep last night?')
    info7 = models.TimeField(
        label='What time did you wake up?')
    info8 = models.TimeField(
        label='What time did you get out of bed?')
    info9 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']],
        label='Did you remove any of the monitors for >10 minutes today?',
        widget=widgets.RadioSelectHorizontal)
