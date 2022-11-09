import pytest
from one_hot_encoder import fit_transform


def test_raises_type_error():
    with pytest.raises(TypeError):
        fit_transform()


@pytest.fixture()
def strings_arr():
    return [('Hello', [0, 1]), ('world', [1, 0])]


def test_string_arr(strings_arr):
    assert fit_transform(['Hello', 'world']) == strings_arr


def test_string(strings_arr):
    assert fit_transform('Hello world') != strings_arr
    # assert fit_transform('Hello world') == [('Hello world', [1])]


def test_fruits():
    assert ('pen', [0, 0, 1]) in fit_transform(['pen', 'pineapple', 'apple', 'pen'])


def test_capital():
    assert fit_transform(['meow', 'Meow']) == [('meow', [0, 1]), ('Meow', [1, 0])]
