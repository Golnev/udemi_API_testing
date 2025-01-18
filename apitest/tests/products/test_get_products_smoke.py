import pytest

from apitest.src.dao.products_dao import ProductsDAO
from apitest.src.helpers.products_helper import ProductsHelper
from apitest.src.utilities.requestsUtilities import RequestUtility

pytestmark = [pytest.mark.products, pytest.mark.smoke]


@pytest.mark.tcid24
def test_get_all_products():
    req_helper = RequestUtility()
    rs_api = req_helper.get(endpoint='products', params={'per_page': 3})

    assert rs_api, f'Response off list products is empty'


@pytest.mark.tcid25
def test_get_product_by_id():
    #  Get a product (test data) from DB.
    rand_product = ProductsDAO().get_random_product_from_db(1)
    rand_product_id = rand_product[0]['ID']
    db_name = rand_product[0]['post_title']

    #  Make the call.
    product_helper = ProductsHelper()
    rs_api = product_helper.get_product_by_id(rand_product_id)
    api_name = rs_api['name']

    #  Verify the response.
    assert db_name == api_name, (f'Get product by ID returned wrong product. '
                                 f'ID: {rand_product_id}, DB name: {db_name}, API name: {api_name}')
