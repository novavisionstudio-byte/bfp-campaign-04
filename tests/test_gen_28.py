from app.gen_28 import value_28


def test_value_28():
    assert value_28(2) == 2 * 9 + 7
    assert value_28(0) == 7
