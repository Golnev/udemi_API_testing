import pytest

from apitest.src.dao.orders_dao import OrdersDAO
from apitest.src.dao.products_dao import ProductsDAO
from apitest.src.helpers.orders_helper import OrdersHelper


@pytest.mark.smoke
@pytest.mark.orders
@pytest.mark.tcid48
def test_create_paid_order_guest_user():
    product_dao = ProductsDAO()
    order_dao = OrdersDAO()
    order_helper = OrdersHelper()

    #  Get a product from DB.
    rand_product = product_dao.get_random_product_from_db(1)
    product_id = rand_product[0]['ID']

    #  Make the call.
    info = {"line_items": [
        {
            "product_id": product_id,
            "quantity": 1
        }
    ]}
    order_json = order_helper.create_order(additional_args=info)

    #  Verify response.
    assert order_json, f'Create order response is empty'
    assert order_json['customer_id'] == 0, (f'Create order as get expected default customer_id=0, '
                                            f'but got {order_json['customer_id']}')
    assert len(order_json['line_items']) == info["line_items"][0]["quantity"], \
        (f'Expected only {info["line_items"][0]["quantity"]} item in order, '
         f'but found {len(order_json['line_items'])}. Order id: {order_json["id"]}.')

    #  Verify DB.
    order_id = order_json["id"]
    line_info = order_dao.get_order_lines_by_order_id(order_id=order_id)
    assert line_info, (f'Create order, line item not found in DB. '
                       f'Order id: {order_id}')

    line_items = [i for i in line_info if i['order_item_type'] == 'line_item']
    assert len(line_items) == info["line_items"][0]["quantity"], (f'Expected {info["line_items"][0]["quantity"]}'
                                                                  f'line item but found {len(line_items)}. '
                                                                  f'Order id: {order_json["id"]}')

    line_id = line_items[0]['order_item_id']
    line_details = order_dao.get_order_items_details(line_id)

    #  For method from course
    # db_product_id = int(line_details['_product_id'])

    db_product_id = line_details[0]['ID']

    assert db_product_id == product_id, (f'Create order "product_id" in DB does not match in API. '
                                         f'API product_id: {product_id}, DB product id: {db_product_id}')
