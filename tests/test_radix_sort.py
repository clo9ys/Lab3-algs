from src.radix_sort import radix_sort

def test_radix_sort():
    assert radix_sort([170, 45, 75, 90, 802, 24, 2, 66]) == [2, 24, 45, 66, 75, 90, 170, 802]
    assert radix_sort([]) == []
    assert radix_sort([52]) == [52]
