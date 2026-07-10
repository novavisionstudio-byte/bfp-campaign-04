from app.gen_37 import value_37


def test_value_37():
    assert value_37(2) == 2 * 3 + 5
    assert value_37(0) == 5
