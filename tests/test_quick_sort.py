from src.quick_sort import quick_sort

def test_quick_sort():
    assert quick_sort([3, 5, 2, 1, 4]) == [1, 2, 3, 4, 5]
    assert quick_sort([]) == []
    assert quick_sort([52]) == [52]
