from src.bucket_sort import bucket_sort
import pytest

@pytest.mark.parametrize("lst, sortd", [
    ([0.12, 0.91, 0.25, 0.31, 0.56], [0.12, 0.25, 0.31, 0.56, 0.91]),
    ([], []),
    ([0.5], [0.5])
])
def test_bucket_sort(lst, sortd):
    assert bucket_sort(lst, len(lst)) == sortd
