import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("3+5", 8),
        ("2+4", 6),
        ("6*9", 54)
    ]
)
def test_answer_2(test_input, expected):
    assert eval(test_input) == expected


def test_simple(fixture_1):
    assert fixture_1 == "hello1"
