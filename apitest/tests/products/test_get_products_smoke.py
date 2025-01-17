import pytest

from apitest.src.utilities.requestsUtilities import RequestUtility


@pytest.mark.products
@pytest.mark.tcid24
def test_get_all_products():
    req_helper = RequestUtility()
    rs_api = req_helper.get(endpoint='products', params={'per_page': 3})

    assert rs_api, f'Response off list products is empty'
