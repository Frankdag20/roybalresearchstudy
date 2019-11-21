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
        choices=[['Choice1', 'Choice1'], ['Choice2', 'Choice2']],
        label='This is an example of the first question?',
        widget=widgets.RadioSelect)
    info2 = models.StringField(
        choices=[['Choice1', 'Choice1'], ['Choice2', 'Choice2']],
        label='Second question?',
        widget=widgets.RadioSelect)
    info3 = models.StringField(
        choices=[['Choice1', 'Choice1'], ['Choice2', 'Choice2']],
        label='Another question?',
        widget=widgets.RadioSelect)
    info4 = models.StringField(
        choices=[['Choice1', 'Choice1'], ['Choice2', 'Choice2']],
        label='More information',
        widget=widgets.RadioSelect)
