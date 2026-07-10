from app.gen_30 import value_30


def test_value_30():
    assert value_30(2) == 2 * 7 + 2
    assert value_30(0) == 2
