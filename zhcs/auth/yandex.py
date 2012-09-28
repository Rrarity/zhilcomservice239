from social_auth.backends.contrib.yandex import *


class FixedYandexOauth2(YandexOAuth2):
    REDIRECT_STATE = False

BACKENDS['yandex-oauth2'] = FixedYandexOauth2
