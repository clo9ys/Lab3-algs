from src.quick_sort import quick_sort

import pytest


@pytest.mark.parametrize("lst, sortd", [
    ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
    ([], []),
    ([52], [52])
])
def test_quick_sort(lst, sortd):
    assert quick_sort(lst) == sortd
