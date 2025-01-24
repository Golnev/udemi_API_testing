import json
import os
from typing import Optional

from apitest.src.dao.orders_dao import OrdersDAO
from apitest.src.utilities.wooAPIUtility import WooAPIUtility


class OrdersHelper:

    def __init__(self):
        self.curr_file_dir = os.path.dirname(os.path.realpath(__file__))
        self.woo_helper = WooAPIUtility()
        self.order_dao = OrdersDAO()

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

    def verify_order_is_created(self, order_json, exp_cust_id, exp_products):
        #  Verify response.
        assert order_json, f'Create order response is empty'
        assert order_json['customer_id'] == exp_cust_id, (
            f'Create order with given customer_id returned bad customer id. '
            f'Expected customer_id: {exp_cust_id}, '
            f'but got {order_json['customer_id']}')

        assert len(order_json['line_items']) == len(exp_products), \
            (f'Expected only {len(exp_products)} item in order, '
             f'but found {len(order_json['line_items'])}. Order id: {order_json["id"]}.')

        #  Verify DB.
        order_id = order_json["id"]
        line_info = self.order_dao.get_order_lines_by_order_id(order_id=order_id)
        assert line_info, (f'Create order, line item not found in DB. '
                           f'Order id: {order_id}')

        line_items = [i for i in line_info if i['order_item_type'] == 'line_item']
        assert len(line_items) == len(exp_products), (
            f'Expected {len(exp_products)}'
            f'line item but found {len(line_items)}. '
            f'Order id: {order_json["id"]}')

        # Get list of products ids in the response.
        api_products_ids = [i['product_id'] for i in order_json['line_items']]

        for product in exp_products:
            assert product['product_id'] in api_products_ids, (
                f'Create order does not have at least 1 expected product in DB. '
                f'Product id: {product['product_id']}. Order id: {order_id}')


if __name__ == '__main__':
    obj = OrdersHelper()
    obj.create_order()
