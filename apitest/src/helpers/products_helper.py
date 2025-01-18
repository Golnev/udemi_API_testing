from apitest.src.utilities.requestsUtilities import RequestUtility


class ProductsHelper:
    def __init__(self):
        self.request_utility = RequestUtility()

    def get_product_by_id(self, product_id: int):
        return self.request_utility.get(f'products/{product_id}')
