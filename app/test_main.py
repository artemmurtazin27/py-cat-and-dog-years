from app.main import get_human_age


def test_should_return_zero_if_age_less_than_fifteen() -> None:
    assert get_human_age(14, 0) == [0, 0]


def test_should_return_one_if_age_between_15_and_23() -> None:
    assert get_human_age(15, 23) == [1, 1]


def test_should_return_two_if_age_between_24_and_27() -> None:
    assert get_human_age(24, 27) == [2, 2]


def test_dog_age_should_be_still_two_if_age_is_28() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_21_and_17_if_age_is_100() -> None:
    assert get_human_age(100, 100) == [21, 17]
