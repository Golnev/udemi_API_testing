import os
from pprint import pprint

from dotenv import load_dotenv
from woocommerce import API

load_dotenv()

wcapi = API(
    url="http://localhost:8080/",
    consumer_key=os.getenv('API_CONSUMER_KEY'),
    consumer_secret=os.getenv('API_CONSUMER_SECRET'),
    version="wc/v3"
)


pprint(wcapi.get('products').json())