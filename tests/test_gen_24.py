from app.gen_24 import value_24


def test_value_24():
    assert value_24(2) == 2 * 9 + 5
    assert value_24(0) == 5
