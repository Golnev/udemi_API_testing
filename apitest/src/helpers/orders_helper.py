import json
import os
from typing import Optional

from apitest.src.utilities.wooAPIUtility import WooAPIUtility


class OrdersHelper:

    def __init__(self):
        self.curr_file_dir = os.path.dirname(os.path.realpath(__file__))
        self.woo_helper = WooAPIUtility()

    def create_order(self, additional_args: Optional[dict] = None):
        payload_template = os.path.join(self.curr_file_dir, '..', 'data', 'create_order_payload.json')

        with open(payload_template) as f:
            payload: dict = json.load(f)

        #  If user adds more info to payload, then update it.
        if additional_args:
            assert isinstance(additional_args, dict), (f'Parameter "additional_args" must be a dictionary, '
                                                       f'but found {type(additional_args)}')
            payload.update(additional_args)

        rs_api = self.woo_helper.post('orders', params=payload, expected_status_code=201)

        return rs_api


if __name__ == '__main__':
    obj = OrdersHelper()
    obj.create_order()
