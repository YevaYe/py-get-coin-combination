from app.main import get_coin_combination


def test_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_only_quarters() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]
    assert get_coin_combination(75) == [0, 0, 0, 3]
    assert get_coin_combination(100) == [0, 0, 0, 4]
    assert get_coin_combination(250) == [0, 0, 0, 10]


def test_only_dimes() -> None:
    assert get_coin_combination(20) == [0, 0, 2, 0]
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_only_nickels() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_only_pennies() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(2) == [2, 0, 0, 0]
    assert get_coin_combination(3) == [3, 0, 0, 0]
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_combinations() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]
    assert get_coin_combination(123) == [3, 0, 2, 4]
    assert get_coin_combination(54) == [4, 0, 0, 2]
    assert get_coin_combination(67) == [2, 1, 1, 2]
