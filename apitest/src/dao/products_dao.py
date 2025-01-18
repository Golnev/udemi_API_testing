import random

from apitest.src.utilities.dbUtility import DBUtility


class ProductsDAO:
    def __init__(self):
        self.db_helper = DBUtility()

    def get_random_product_from_db(self, qty: int = 1):
        sql = 'SELECT * FROM wp_posts wp WHERE post_type = "product" LIMIT 5000;'
        rs_sql = self.db_helper.execute_select(sql=sql)

        return random.sample(rs_sql, qty)
