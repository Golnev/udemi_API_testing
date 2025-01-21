import random

from apitest.src.utilities.dbUtility import DBUtility


class ProductsDAO:
    def __init__(self):
        self.db_helper = DBUtility()

    def get_random_product_from_db(self, qty: int = 1) -> list[dict]:
        sql = 'SELECT * FROM wp_posts wp WHERE post_type = "product" LIMIT 5000;'
        rs_sql = self.db_helper.execute_select(sql=sql)

        return random.sample(rs_sql, qty)

    def get_product_by_id_from_db(self, product_id: int):
        sql = f'SELECT * FROM wp_posts wp  WHERE ID = {product_id};'
        return self.db_helper.execute_select(sql=sql)

    def get_products_get_after_given_date(self, _date):
        sql = (f'SELECT * FROM wp_posts WHERE post_date > "{_date}" and post_type = "product" '
               f'ORDER BY post_date DESC limit 10000;')
        return self.db_helper.execute_select(sql=sql)
