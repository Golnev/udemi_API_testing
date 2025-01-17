import logging as logger
import json
import os
from typing import Optional

import requests
from dotenv import load_dotenv
from requests_oauthlib import OAuth1

from apitest.src.configs.hosts_config import API_HOSTS
from apitest.src.utilities.credentialsUtilities import CredentialUtility

load_dotenv()


class RequestUtility:

    def __init__(self):
        self.rs_api = None
        self.rs_json = None
        self.expected_status_code = None
        self.url = None
        self.status_code = None

        wc_creds = CredentialUtility.get_wc_api_keys()

        self.__env = os.getenv('ENV', 'test')
        self.base_url: str = API_HOSTS[self.__env]
        self.auth = OAuth1(wc_creds['wc_key'], wc_creds['wc_secret'])

    def __assert_status_code(self):
        assert self.status_code == self.expected_status_code, \
            (f'Bad status code. Expected status code: {self.expected_status_code}, '
             f'actual status code: {self.rs_api.status_code}, '
             f'URL: {self.url}, Response JSON: {self.rs_json}')

    def post(self, endpoint: str,
             payload: Optional[dict] = None,
             headers: Optional[dict] = None,
             expected_status_code=200):
        if not headers:
            headers = {'Content-Type': 'application/json'}

        self.url: str = self.base_url + endpoint

        self.rs_api = requests.post(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = self.rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = self.rs_api.json()

        self.__assert_status_code()

        logger.debug(f'POST API response: {self.rs_json}')

        return self.rs_json

    def get(self, endpoint: str,
            payload: Optional[dict] = None,
            headers: Optional[dict] = None,
            params: Optional[dict] = None,
            expected_status_code=200):

        if not headers:
            headers = {'Content-Type': 'application/json'}

        self.url: str = self.base_url + endpoint

        rs_api = requests.get(url=self.url, params=params, data=json.dumps(payload), headers=headers, auth=self.auth)

        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()

        self.__assert_status_code()

        logger.debug(f'GET API response: {self.rs_json}')

        return self.rs_json


if __name__ == '__main__':
    cl = RequestUtility()
    print(cl.base_url)
