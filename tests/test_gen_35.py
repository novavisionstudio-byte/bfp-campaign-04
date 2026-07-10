from app.gen_35 import value_35


def test_value_35():
    assert value_35(2) == 2 * 5 + 4
    assert value_35(0) == 4
