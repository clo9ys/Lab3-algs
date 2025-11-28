from src.counting_sort import counting_sort
import pytest

@pytest.mark.parametrize("lst, sortd", [
    ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
    ([], []),
    ([52], [52])
])
def test_counting_sort(lst, sortd):
    assert counting_sort(lst) == sortd
