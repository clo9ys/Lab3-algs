from src.heap_sort import heap_sort
import pytest

@pytest.mark.parametrize("lst, sortd", [
    ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
    ([], []),
    ([52], [52])
])
def test_heap_sort(lst, sortd):
    assert heap_sort(lst) == sortd
