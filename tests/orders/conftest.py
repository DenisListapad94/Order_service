import pytest


@pytest.fixture(scope="module")
def fixture_1():
    some_str = "hello1"
    print(some_str)
    return some_str
