import os

from dotenv import load_dotenv

load_dotenv()

class CredentialUtility:
    def __init__(self):
        pass

    @staticmethod
    def get_wc_api_keys():

        wc_key = os.getenv('API_CONSUMER_KEY')
        wc_secret = os.getenv('API_CONSUMER_SECRET')

        if not wc_key or not wc_secret:
            raise Exception('The API credentials "API_CONSUMER_KEY" and "API_CONSUMER_SECRET" must be in env variable')
        else:
            return {'wc_key': wc_key, 'wc_secret': wc_secret}


    @staticmethod
    def get_db_credentials():

        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')

        if not db_user or not db_password:
            raise Exception('The DB credentials "DB_USER" and "DB_PASSWORD" must be in env variable')
        else:
            return {'db_user': db_user, 'db_password': db_password}


if __name__ == '__main__':
    cred = CredentialUtility.get_wc_api_keys()
    print(cred)
