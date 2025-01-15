import pytest

pytestmark = [pytest.mark.be, pytest.mark.slow]


@pytest.fixture(scope='module')
def my_setup():
    print('')
    print('>>> MY SETUP <<<')

    return {'id': 20, 'name': 'Admas'}


@pytest.mark.smoke
@pytest.mark.ll
def test_login_page_valid_user(my_setup):
    print('\nLogin with valid user')
    print('Func: a')

    print(f'Name: {my_setup.get("name")}')

    # import pdb
    # pdb.set_trace()


@pytest.mark.regression
def test_login_test_wrong_pass(my_setup):
    print('Login wrong pass')
    print('Func: b')
    # assert 1==2, 'Error, 1 is not 2'
