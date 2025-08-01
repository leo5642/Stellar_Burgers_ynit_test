import pytest

class UrlCollector:
    url_home = 'https://stellarburgers.nomoreparties.site/'

    url_register = url_home + 'api/auth/register'
    url_login = url_home + 'api/auth/login'
    url_order = url_home + 'api/orders'
