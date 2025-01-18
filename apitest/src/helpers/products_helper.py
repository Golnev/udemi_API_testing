import logging as logger
from typing import Optional

from apitest.src.utilities.requestsUtilities import RequestUtility


class ProductsHelper:
    def __init__(self):
        self.request_utility = RequestUtility()

    def get_product_by_id(self, product_id: int):
        return self.request_utility.get(f'products/{product_id}')

    def call_create_product(self, payload):
        return self.request_utility.post(endpoint='products', payload=payload, expected_status_code=201)

    def call_list_products(self, payload: Optional[dict] = None):
        max_pages = 1000
        all_products = []
        for i in range(1, max_pages + 1):

            if not 'per_page' in payload.keys():
                payload['per_page'] = 100

            #  Add the current page number to the call.
            payload['page'] = i
            rs_api = self.request_utility.get(endpoint='products', payload=payload)

            #  If there is no response then stop loop b/c there are no products.
            if not rs_api:
                break
            else:
                all_products.extend(rs_api)

            logger.debug(f'List products page number: {i}')

        else:
            raise Exception(f'Unable to find all products after {max_pages} pages.')

        return all_products
