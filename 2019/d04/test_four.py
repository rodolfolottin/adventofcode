import pytest

from four import match_criterias, match_criterias_part_2


@pytest.mark.parametrize(
    "password, is_valid", [("223450", False), ("111111", True), ("123789", False),]
)
def test_match_criterias(password, is_valid):
    assert match_criterias(password) == is_valid


@pytest.mark.parametrize(
    "password, is_valid",
    [
        ("112233", True),
        ("123444", False),
        ("111122", True),
        ("568999", False),
        ("344446", False),
    ],
)
def test_match_criterias_part_2(password, is_valid):
    assert match_criterias_part_2(password) == is_valid
