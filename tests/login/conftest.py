from pytest import fixture

from dto.test_user import TestUser


@fixture
def valid_user(scope='function'):
    yield TestUser()
