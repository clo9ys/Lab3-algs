from src.bubble_sort import bubble_sort

def test_bubble_sort():
    assert bubble_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
    assert bubble_sort([]) == []
    assert bubble_sort([52]) == [52]
