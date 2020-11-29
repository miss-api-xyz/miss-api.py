import requests
from src import config

class MissAgent:
    def __init__(self, APIKEY=None):
        self.key = APIKEY
        if not self.key:
            raise Exception("Specify API-KEY. Documentation: https://github.com/miss-api-xyz/miss-api.py")

    def get(self, endpoint=None):

        if not endpoint:
            raise Exception("Specify an available endpoint. Documentation: https://github.com/miss-api-xyz/miss-api.py")

        return req(endpoint, headers = 
            { 
                "Content-Type": "application/json",
                "Authorization": f"{self.key}" 
            } 
        )

def req(endpoint, headers):
    res = requests.get(f"{config.url}/api/{config.APIversion}/{endpoint}", headers=headers)
    return res.json()

# Developer with ❤ by miss-api Team #
