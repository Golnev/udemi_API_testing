from datetime import datetime, timedelta

import pytest

from apitest.src.dao.products_dao import ProductsDAO
from apitest.src.helpers.products_helper import ProductsHelper


@pytest.mark.regression
class TestListProductsWithFilter:

    @pytest.mark.tcid51
    def test_list_products_with_filter_after(self):
        #  Create data.
        x_days_from_today = 300
        _after_created_date = datetime.now().replace(microsecond=0) - timedelta(days=x_days_from_today)
        after_created_date = _after_created_date.isoformat()

        #  Same:
        # tmp_date = datetime.now() - timedelta(days=x_days_from_today)
        # after_created_date = tmp_date.strftime('%Y-%M-%dT%H:%m:%S')

        payload = dict()
        payload['after'] = after_created_date
        # payload['per_page'] = 100
        payload['orderby'] = 'id'

        #  Make the call.
        rs_api = ProductsHelper().call_list_products(payload=payload)
        assert rs_api, f'Empty response for "list products with filter"'

        #  Get data from DB.
        db_products = ProductsDAO().get_products_get_after_given_date(after_created_date)

        #  Verify response.
        assert len(rs_api) == len(db_products), \
            (f'Count of products with filter "after" from the API does not match the count from the DB. '
             f'API count: {len(rs_api)}, DB count: {len(db_products)}')

        ids_in_api = [i['id'] for i in rs_api]
        ids_in_db = [i['ID'] for i in db_products]

        # assert ids_in_db == ids_in_api

        ids_diff = list(set(ids_in_api) - set(ids_in_db))

        assert not ids_diff, f'List products with filter. Products ids in response mismatch in DB.'
