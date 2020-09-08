from datetime import datetime

import pytest

from hero import hero

''' Fixtures are used when we want to run some code before every test method. So instead of repeating the same code in every test we define fixtures. Usually, fixtures are used to initialize database connections, pass the base , etc '''

@pytest.fixture(scope="function")
def dummy_data():
    print("making dummy data")
    return hero("Thor", datetime(1981, 8, 13), "Thunder")


def test_thor_get_age(dummy_data):
    thor_age = (datetime.now() - dummy_data.date).days // 365
    assert dummy_data.get_age() == dummy_data_age


def test_thor_add_movies(dummy_data):
    dummy_data.add_movies(5)
    assert dummy_data.get_credits() == 5


def test_thor_get_flop(dummy_data):
    assert dummy_data.get_movies() == 0
