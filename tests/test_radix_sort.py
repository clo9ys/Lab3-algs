from src.radix_sort import radix_sort
import pytest

@pytest.mark.parametrize("lst, sortd", [
    ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
    ([], []),
    ([52], [52])
])
def test_radix_sort(lst, sortd):
    assert radix_sort(lst) == sortd
