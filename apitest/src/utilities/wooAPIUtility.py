import logging as logger
import os
from typing import Optional

from dotenv import load_dotenv
from woocommerce import API

# from apitest.src.configs.hosts_config import WOO_API_HOSTS
from apitest.src.configs.hosts_config import WOO_API_HOSTS
from apitest.src.utilities.credentialsUtilities import CredentialUtility

load_dotenv()


class WooAPIUtility:
    def __init__(self):
        self.url = None
        self.rs_json = None
        self.expected_status_code = None
        self.status_code = None
        self.rs_api = None

        wc_creds = CredentialUtility.get_wc_api_keys()

        self.__env = os.getenv('ENV', 'test')
        self.base_url: str = WOO_API_HOSTS[self.__env]

        self.wcapi = API(
            url=self.base_url,
            consumer_key=wc_creds['wc_key'],
            consumer_secret=wc_creds['wc_secret'],
            version="wc/v3"
        )

    def __assert_status_code(self):
        assert self.status_code == self.expected_status_code, \
            (f'Bad status code. Expected status code: {self.expected_status_code}, '
             f'actual status code: {self.rs_api.status_code}, '
             f'URL: {self.url}, Response JSON: {self.rs_json}')

    def get(self, wc_endpoint: str, params: Optional[dict] = None, expected_status_code: int = 200):
        self.url: str = self.base_url + wc_endpoint

        self.rs_api = self.wcapi.get(endpoint=wc_endpoint, params=params)

        self.status_code = self.rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = self.rs_api.json()

        self.__assert_status_code()

        logger.debug(f'GET API response: {self.rs_json}')

        return self.rs_json


if __name__ == '__main__':
    obj = WooAPIUtility()
    rs_api = obj.get('products', params={'per_page': 2})
    print(rs_api)

    import pdb

    pdb.set_trace()
