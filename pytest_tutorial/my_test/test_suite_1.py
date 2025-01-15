import pytest

pytestmark = [pytest.mark.fe, pytest.mark.slow]


@pytest.mark.smoke
def test_login_page_valid_user():
    print('Login test')
    print('Func: a')


@pytest.mark.regression
def test_login_test_wrong_pass():
    print('Login wrong pass')
    print('Func: b')
    assert 1==2, 'Error, 1 is not 2'
