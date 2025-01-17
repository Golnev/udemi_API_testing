import random

from apitest.src.utilities.dbUtility import DBUtility


class CustomersDAO:

    def __init__(self):
        self.__db_helper = DBUtility()

    def get_customer_by_email(self, email: str):
        sql = f'SELECT * FROM wp_users WHERE user_email = "{email}";'
        rs_sql = self.__db_helper.execute_select(sql=sql)

        return rs_sql

    def get_random_customer_from_db(self, qty: int = 1):
        sql = 'SELECT * FROM wp_users wu ORDER BY id DESC LIMIT 5000;'
        rs_sql = self.__db_helper.execute_select(sql=sql)

        return random.sample(rs_sql, qty)
