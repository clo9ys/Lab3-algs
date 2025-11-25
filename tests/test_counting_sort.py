from src.counting_sort import counting_sort

def test_counting_sort():
    assert counting_sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]
    assert counting_sort([]) == []
    assert counting_sort([52]) == [52]
