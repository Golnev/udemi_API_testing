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


if __name__ == '__main__':
    em, passw = generate_random_email_and_password().values()
    print(em, passw)