from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = ['info1', 'info2']
    timeout_seconds = 60

class MyPage2(Page):
    form_model = 'player'
    form_fields = ['info3', 'info2']
    timeout_seconds = 60

class MyPage3(Page):
    form_model = 'player'
    form_fields = ['info1', 'info4']
    timeout_seconds = 60

class MyPage4(Page):
    form_model = 'player'
    form_fields = ['info1', 'info2']
    timeout_seconds = 60

class MyPage5(Page):
    form_model = 'player'
    form_fields = ['info1', 'info2']
    timeout_seconds = 60


class Results(Page):
    pass


page_sequence = [MyPage, MyPage2, MyPage3, MyPage4, MyPage5]
