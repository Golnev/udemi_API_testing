import logging as logger
from typing import Optional

from faker import Faker


def generate_random_email_and_password(domain: Optional[str] = None) -> dict[str, str]:
    logger.debug('Generate random email and password')

    fake = Faker()

    email = fake.email(domain=domain)
    password = fake.password(length=8, special_chars=False)

    random_info = {'email': email, 'password': password}

    logger.debug(f'Randomly generated email and password: {random_info}')

    return random_info


def generate_random_product_name(prefix: Optional[str] = None, suffix: Optional[str] = None):
    logger.debug('Generate random product name')

    fake = Faker()
    product_name = fake.word()

    if prefix:
        product_name = prefix + product_name
    if suffix:
        product_name = product_name + suffix

    return product_name

if __name__ == '__main__':
    # em, passw = generate_random_email_and_password().values()
    # print(em, passw)
    pr_name = generate_random_product_name(prefix='test_', suffix='_test')
    print(pr_name)