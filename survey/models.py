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
    info1 = models.StringField(
        choices=[['Press when you have thought of a situation.', 'Press when you have thought of a situation.']],
        label='Think of  a time in the future when you were inspired by family and friends.',
        widget=widgets.RadioSelect)
    info2 = models.StringField(
        choices=[['New', 'New'], ['Old', 'Old']],
        label='You are more likely to live longer and enjoy people and things you love if you start to sit less.',
        widget=widgets.RadioSelect)
    info3 = models.StringField(
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5']],
        label='Think of nearby places you go often. Try walking to these places instead of driving. How likely are you to do this in your daily life? (1 unlikely - 5 very likely)',
        widget=widgets.RadioSelect)
    info4 = models.StringField(
        choices=[['😄', '😄'], ['🙂', '🙂'], ['😐', '😐'], ['🙁', '🙁'], ['😧', '😧']],
        label='Mood?',
        widget=widgets.RadioSelect)
