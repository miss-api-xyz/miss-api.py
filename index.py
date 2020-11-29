import requests
from src import config

class MissAgent:
    def __init__(self, APIKEY):
        self.key = APIKEY

    def get(self, endpoint):
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