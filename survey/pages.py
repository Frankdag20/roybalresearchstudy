from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants
import time

class MyPage(Page):
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        # user has 5 minutes to complete as many pages as possible
        self.participant.vars['expiry'] = time.time() + 1 * 60
    form_model = 'player'
    form_fields = ['age', 'gender']


class MyPage2(Page):
    form_model = 'player'
    form_fields = ['crt_bat', 'crt_widget', 'crt_lake']
    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3

page_sequence = [Demographics, CognitiveReflectionTest]
