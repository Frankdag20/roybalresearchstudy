from os import environ


SESSION_CONFIGS = [

    dict(
        name='survey',
        num_demo_participants=140,
        app_sequence=['survey'],
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='roybal',
        display_name='DASH Research Study',
        participant_label_file='participantList.txt',
        use_secure_urls=True
    )
]

ADMIN_USERNAME = 'dash'
# for security, best to set admin password in an environment variable

#ADMIN_PASSWORD = '123'
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

# don't share this with anybody.
SECRET_KEY = '+hj8s7d@ch3#pf^9=^yaznkl0suf3gkt5a%3+7%ljxvw0592r@'

INSTALLED_APPS = ['otree']
