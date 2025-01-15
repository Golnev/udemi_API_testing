import pytest

pytestmark = [pytest.mark.fe, pytest.mark.slow]


@pytest.fixture(scope='module')
def my_setup():
    print('')
    print('>>> MY SETUP <<<')

    return {'id': 20, 'name': 'Admas'}


@pytest.mark.abc
class TestCheckout:

    def test_checkout_as_guest(self, my_setup):
        print('\n')
        print('Checkout as guest')
        print('Class method: 1')

    def test_checkout_with_existing_user(self):
        print('\n')
        print('Checkout as user')
        print('Class method: 2')
