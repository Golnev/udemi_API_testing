import logging as logger
import os
from typing import TypedDict

import pymysql
from dotenv import load_dotenv

from apitest.src.utilities.credentialsUtilities import CredentialUtility

load_dotenv()


class DbCredentials(TypedDict):
    db_user: str
    db_password: str


class DBUtility:

    def __init__(self):
        self.creds: DbCredentials = CredentialUtility.get_db_credentials()
        self.port = int(os.getenv('DB_PORT'))
        self.host = os.getenv('DB_HOST')
        self.database = os.getenv('DB_DATABASE')

    def __create_connection(self):
        connection = pymysql.connect(host=self.host,
                                     user=self.creds['db_user'],
                                     password=self.creds['db_password'],
                                     database=self.database,
                                     port=self.port)
        return connection

    def execute_select(self, sql):
        conn = self.__create_connection()

        try:
            logger.debug(f'Executing: {sql}')
            with conn.cursor(pymysql.cursors.DictCursor) as cur:
                cur.execute(sql)
                rs_dict = cur.fetchall()
                return rs_dict
        except Exception as e:
            raise Exception(f'Failed running sql: {sql}. Error: {str(e)}')
        finally:
            conn.close()

    def execute_sql(self, sql):
        pass
