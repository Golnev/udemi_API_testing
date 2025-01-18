from apitest.src.utilities.requestsUtilities import RequestUtility


class ProductsHelper:
    def __init__(self):
        self.request_utility = RequestUtility()

    def get_product_by_id(self, product_id: int):
        return self.request_utility.get(f'products/{product_id}')

    def call_create_product(self, payload):
        return self.request_utility.post(endpoint='products', payload=payload, expected_status_code=201)
