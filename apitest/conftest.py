import logging


def pytest_configure():
    logging.getLogger('faker').setLevel(logging.WARNING)
    logging.getLogger('requests_oauthlib').setLevel(logging.WARNING)
    logging.getLogger('requests').setLevel(logging.WARNING)
    logging.getLogger('urllib3').setLevel(logging.WARNING)
    logging.getLogger('oauthlib').setLevel(logging.WARNING)