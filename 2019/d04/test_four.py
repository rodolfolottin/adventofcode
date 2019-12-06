import pytest

from four import match_criteria


@pytest.mark.parametrize(
    "password, is_valid", [("223450", False), ("111111", True), ("123789", False),]
)
def test_match_criterias(password, is_valid):
    assert match_criteria(password) == is_valid
