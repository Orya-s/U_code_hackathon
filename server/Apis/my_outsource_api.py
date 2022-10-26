import json
from .api import Api
from database import fetcher

class MyOutsourceApi(Api):

    def __init__(self, base_url= ""):
        super().__init__()
        self.url = base_url

    def make_call(self, method = "GET", resources = "", headers = {"Content-Type": "application/json"}):
        self.headers = headers
        self.resources = resources
        self.method = method
        return super().make_call()

    #note, make it more pythonic later
    def proccess_data(self, isGluten=False, isDiary=False):
        pass