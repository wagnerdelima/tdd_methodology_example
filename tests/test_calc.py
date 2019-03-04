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


def test_subtract_two_numbers():
    c = Calc()

    res = c.sub(9, 5)
    assert res == 4


def test_mul_two_numbers():
    c = Calc()

    res = c.mul(2, 4)
    assert res == 8


def test_mul_many_numbers():
    numbers = range(1, 10)

    c = Calc()

    res = c.mul(*numbers)
    assert res == 362880
