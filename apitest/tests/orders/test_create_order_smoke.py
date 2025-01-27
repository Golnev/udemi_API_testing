import pytest

from apitest.src.dao.products_dao import ProductsDAO
from apitest.src.helpers.customers_helper import CustomerHelper
from apitest.src.helpers.orders_helper import OrdersHelper


@pytest.fixture(scope="module")
def my_orders_smoke_setup():
    product_dao = ProductsDAO()

    rand_product = product_dao.get_random_product_from_db(1)
    product_id = rand_product[0]['ID']

    order_helper = OrdersHelper()

    info = {'product_id': product_id, 'order_helper': order_helper}

    return info


@pytest.mark.smoke
@pytest.mark.orders
@pytest.mark.tcid48
def test_create_paid_order_guest_user(my_orders_smoke_setup):
    #  Create helper objects.
    order_helper = my_orders_smoke_setup['order_helper']

    customer_id = 0
    product_id = my_orders_smoke_setup['product_id']


    #  Make the call.
    info = {"line_items": [
        {
            "product_id": product_id,
            "quantity": 1
        }
    ]}
    order_json = order_helper.create_order(additional_args=info)

    #  Verify response.
    expected_products = [{'product_id': product_id}]
    order_helper.verify_order_is_created(order_json=order_json, exp_cust_id=customer_id, exp_products=expected_products)


@pytest.mark.smoke
@pytest.mark.orders
@pytest.mark.tcid49
def test_create_paid_order_new_created_customer(my_orders_smoke_setup):
    #  Create helper objects.
    order_helper = my_orders_smoke_setup['order_helper']
    customer_helper = CustomerHelper()

    #  Make the call.
    cust_info = customer_helper.create_customer()
    customer_id = cust_info['id']
    product_id = my_orders_smoke_setup['product_id']

    info = {"line_items": [
        {
            "product_id": product_id,
            "quantity": 1
        }
    ],
        'customer_id': customer_id
    }
    order_json = order_helper.create_order(additional_args=info)

    #  Verify response.
    expected_products = [{'product_id': product_id}]
    order_helper.verify_order_is_created(order_json=order_json, exp_cust_id=customer_id, exp_products=expected_products)
