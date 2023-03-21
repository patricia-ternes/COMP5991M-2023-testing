import src.functions as fc

"""
Function name: fc.even_odd(n)
Return
- "Even"
- "Odd"

Scenarios:
- Not int: return "Yellow"
- Zero: "https://www.britannica.com/story/is-zero-an-even-or-an-odd-number"
- Odd: 7==Odd
- Even 2==Even
- Odd_larger: 56412382181 == Odd
- Even_larger: 87187789512 == Even
- Negative Odd: -7==Odd
- Negative Even -2==Even
- Negative Odd_larger: -56412382181 == Odd
- Negative Even_larger: -87187789512 == Even
"""


def test_type():
    assert fc.even_odd("a") == "Yellow"
    assert fc.even_odd(1.0) == "Yellow"
    assert fc.even_odd([1, 2, 6]) == "Yellow"
    assert fc.even_odd({1, 2, 6}) == "Yellow"


def test_zero():
    assert (
        fc.even_odd(0)
        == "https://www.britannica.com/story/is-zero-an-even-or-an-odd-number"
    )


def test_odd_small():
    assert fc.even_odd(7) == "Odd"


def test_even_small():
    assert fc.even_odd(2) == "Even"


def test_odd_large():
    assert fc.even_odd(56412382181) == "Odd"


def test_even_large():
    assert fc.even_odd(87187789512) == "Even"


def test_odd_small_negative():
    assert fc.even_odd(-7) == "Odd"


def test_even_small_negative():
    assert fc.even_odd(-2) == "Even"


def test_odd_large_negative():
    assert fc.even_odd(-56412382181) == "Odd"


def test_even_large_negative():
    assert fc.even_odd(-87187789512) == "Even"
