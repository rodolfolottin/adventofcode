import pytest

from one import fuel_requirement, fuel_requirement_fuel


@pytest.mark.parametrize(
    "number, expected", [(12, 2), (14, 2), (1969, 654), (100756, 33583),]
)
def test_fuel_requirement(number, expected):
    assert fuel_requirement(number) == expected


@pytest.mark.parametrize("number, expected", [(12, 2), (1969, 966), (100756, 50346),])
def test_fuel_requirement_fuel(number, expected):
    assert fuel_requirement_fuel(number) == expected
