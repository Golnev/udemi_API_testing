import pytest

from apitest.src.utilities.requestsUtilities import RequestUtility


@pytest.mark.tcid30
def test_get_all_customers():
    req_helper = RequestUtility()
    rs_api = req_helper.get(endpoint='customers', params={'orderby': 'registered_date', 'order': 'desc', 'per_page': 3})

    assert rs_api, f'Response off list customers is empty'
