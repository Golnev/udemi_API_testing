from apitest.src.utilities.dbUtility import DBUtility


class CustomersDAO:

    def __init__(self):
        self.__db_helper = DBUtility()

    def get_customer_by_email(self, email: str):
        sql = f'SELECT * FROM wp_users WHERE user_email = "{email}";'
        rs_sql = self.__db_helper.execute_select(sql=sql)

        return rs_sql
