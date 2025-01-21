from apitest.src.utilities.dbUtility import DBUtility


class OrdersDAO:
    def __init__(self):
        self.db_helper = DBUtility()

    def get_order_lines_by_order_id(self, order_id: int):
        sql = f'SELECT * FROM wp_woocommerce_order_items WHERE order_id={order_id};'
        return self.db_helper.execute_select(sql=sql)

    def get_order_items_details(self, item_id: int):
        sql = (f'SELECT p.* FROM wordpress_db.wp_woocommerce_order_itemmeta oi '
               f'JOIN wp_posts p ON oi.meta_value = p.ID '
               f'WHERE order_item_id = {item_id} AND meta_key = "_product_id";')

        return self.db_helper.execute_select(sql=sql)

        #  Method from course:
        # sql = f'SELECT * FROM wordpress_db.wp_woocommerce_order_itemmeta WHERE order_item_id = {item_id};'
        #
        # rs_sql = self.db_helper.execute_select(sql=sql)
        #
        # line_details = dict()
        # for meta in rs_sql:
        #     line_details[meta['meta_key']] = meta['meta_value']
        #
        # return line_details
