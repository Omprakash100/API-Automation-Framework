import requests
from config.config import Config


class RequestHandler:
    base_url = Config.BASE_URL

    @classmethod
    def send_request(cls, method, endpoint, headers=None, params=None, json_data=None, data=None):
        url = f"{cls.base_url}/{endpoint}"
        response = requests.request(method, url, headers=headers, params=params, json=json_data, data=data)
        return response
