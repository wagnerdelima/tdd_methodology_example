from ..calc.calc import Calc


def test_add_two_numbers():
    c = Calc()

    res = c.add(4, 5)
    assert res == 9


def test_add_many_numbers():
    numbers = range(100)

    c = Calc()

    res = c.add(*numbers)
    assert res == 4950
