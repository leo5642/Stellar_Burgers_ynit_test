import pytest
import requests
import random
import string

class AuthData():
    login = [
        ("login", "Недостаточно данных для создания учетной записи"),
        ("password", "Недостаточно данных для создания учетной записи"),
    ]
    
    my_register = {
        "email": "leo5642@tets.ru",
        "password": "sdfsdfsdf",
        "name":  "leo5642"
    }

    my_login = {
        "email": "leo5642@tets.ru",
        "password": "sdfsdfsdf"
    }

    my_access_token = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY4OGNlNjc2OWVkMjgwMDAxYjY2YTI0ZCIsImlhdCI6MTc1NDA2NTIxOCwiZXhwIjoxNzU0MDY2NDE4fQ.naoHvNIsPwz-WpWgnao96UzHUW4OJj84FQsWJQ0GZXA'
    my_refresh_token = '30cf0a53f67feec32225b9c4b17c13d3c597f617efac9c1de941a162310ef664a7b619e7ee16ba1c'
    headers = {
    "Content-Type": "application/json",
    "Authorization": my_refresh_token
    }

    my_order = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    }

