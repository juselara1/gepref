import pytest
from gepref.list import IdentityStep, SquareStep

@pytest.mark.parametrize("length", range(5, 15))
def test_identity(length: int):
    data = list(range(length))
    tr_data = IdentityStep()(data)
    assert all(map(lambda case: case[0] == case[1], zip(data, tr_data)))

@pytest.mark.parametrize("length", range(5, 15))
def test_square(length: int):
    data = list(range(length))
    tr_data = SquareStep()(data)
    assert all(map(lambda case: case[0] ** 2 == case[1], zip(data, tr_data)))
