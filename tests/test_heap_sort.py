from src.heap_sort import heap_sort

def test_heap_sort():
    assert heap_sort([3, 7, 1, 5, 2]) == [1, 2, 3, 5, 7]
    assert heap_sort([]) == []
    assert heap_sort([52]) == [52]
