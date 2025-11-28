from src.bubble_sort import bubble_sort
import pytest

@pytest.mark.parametrize("lst, sortd", [
    ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
    ([], []),
    ([52], [52])
])
def test_bubble_sort(lst, sortd):
    assert bubble_sort(lst) == sortd