from typing import Optional

from apitest.src.utilities.genericUtilities import generate_random_email_and_password
from apitest.src.utilities.requestsUtilities import RequestUtility


class CustomerHelper:
    def __init__(self):
        self.request_utility = RequestUtility()

    def create_customer(self, email: Optional[str] = None, password: Optional[str] = None, **kwargs):

        if not email:
            ep = generate_random_email_and_password()
            email = ep['email']
        if not password:
            password = 'test_password'

        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)

        create_user_json = self.request_utility.post('customers', payload=payload, expected_status_code=201)

        return create_user_json
