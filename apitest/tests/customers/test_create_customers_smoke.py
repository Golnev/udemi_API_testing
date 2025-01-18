import pytest
import logging as logger

from faker.proxy import Faker

from apitest.src.dao.customers_dao import CustomersDAO
from apitest.src.helpers.customers_helper import CustomerHelper
from apitest.src.utilities.genericUtilities import generate_random_email_and_password
from apitest.src.utilities.requestsUtilities import RequestUtility

pytestmark = [pytest.mark.customers, pytest.mark.smoke]


@pytest.mark.tcid29
def test_create_customer_only_email_password(faker: Faker):
    logger.info('TEST: Create new customer with email and password only.')

    # With Faker fixture
    # email: str = faker.email()
    # password: str = faker.password(length=6, special_chars=False, upper_case=False)
    # name: str = faker.user_name()
    #
    # logger.info(f'Fake user email: {email}, fake user name: {name}')

    rand_info = generate_random_email_and_password()
    logger.info(rand_info)

    email = rand_info['email']
    password = rand_info['password']

    # # create payload
    # payload = {'email': email, 'password': password}

    # make the call
    cust_obj = CustomerHelper()
    cust_api_info = cust_obj.create_customer(email=email, password=password)

    # verify email and first_name in the response
    assert cust_api_info['email'] == email, f'Create customer API return wrong email. Email: {email}'
    assert cust_api_info['first_name'] == '', (f'Create customer API return value for first name, '
                                               f'but it should be empty.')

    # verify customer is created in DB
    cust_dao = CustomersDAO()
    cust_info = cust_dao.get_customer_by_email(email=email)

    id_in_api = cust_api_info['id']
    id_in_db = cust_info[0]['ID']
    assert id_in_api == id_in_db, (f'Create customer response "id" not same as "ID" in database.'
                                   f'Email: {email}')

    # import pdb
    # pdb.set_trace()


@pytest.mark.tcid47
def test_create_customer_fail_for_existing_email():
    #  Get existing email from DB.
    cust_dao = CustomersDAO()
    existing_cust = cust_dao.get_random_customer_from_db()
    existing_email = existing_cust[0]['user_email']

    # Try to create customer with existing email
    req_helper = RequestUtility()

    payload = {'email': existing_email, 'password': 'password_tcid47'}
    cust_api_info = req_helper.post(endpoint='customers', payload=payload, expected_status_code=400)

    assert cust_api_info['code'] == 'registration-error-email-exists', (f'Create customer with existing user '
                                                                        f'error "cose" is not correct. '
                                                                        f'Expected: "registration-error-email-exists", '
                                                                        f'Actual: {cust_api_info['code']}')
