import pytest

from apitest.src.dao.products_dao import ProductsDAO
from apitest.src.helpers.products_helper import ProductsHelper
from apitest.src.utilities.genericUtilities import generate_random_product_name

pytestmark = [pytest.mark.products, pytest.mark.smoke]


@pytest.mark.tcid26
def test_create_1_simple_product():
    #  Generate some data.
    payload = dict()
    payload['name'] = generate_random_product_name()
    payload['type'] = 'simple'
    payload['regular_price'] = '10.99'

    #  Make the call.
    product_rs = ProductsHelper().call_create_product(payload=payload)

    #  Verify the response is not empty.
    assert product_rs, f'Create product API response is empty. Payload: {payload}'
    assert product_rs['name'] == payload['name'], (f'Create product API call response has unexpected name. '
                                                   f'Expected: {payload['name']}, Actual: {product_rs['name']}')

    #  Verify the product exist in DB.
    product_from_db = ProductsDAO().get_product_by_id_from_db(product_rs['id'])
    assert product_from_db[0]['post_title'] == payload['name'], (f'Create product title in DB does not match '
                                                                 f'title  in API. '
                                                                 f'DB title: {product_from_db[0]['post_title']}, '
                                                                 f'API title: {payload['name']}')
