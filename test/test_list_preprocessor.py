import pytest
from gepref.list import IdentityStep, SquareStep, ListPreprocessor

class TestListPreprocessor:
    @pytest.mark.parametrize("length", range(5, 15))
    def test_simple(self, length: int) -> None:
        data = list(range(length))
        tr_data = ListPreprocessor(steps=[IdentityStep()])(data)
        assert all(map(lambda case: case[0] == case[1], zip(data, tr_data)))

    @pytest.mark.parametrize("length, depth", list(zip(range(10, 15), range(1, 5))))
    def test_multi(self, length: int, depth: int) -> None:
        data = list(range(length))
        tr_data = ListPreprocessor(
            steps=[
                SquareStep()
                for _ in range(depth)
            ],
        )(data)
        assert all(map(lambda case: case[0] ** (2 ** depth) == case[1], zip(data, tr_data)))
