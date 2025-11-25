from src.bucket_sort import bucket_sort

def test_bucket_sort():
    assert bucket_sort([0.12, 0.91, 0.25, 0.31, 0.56], 5) == [0.12, 0.25, 0.31, 0.56, 0.91]
    assert bucket_sort([]) == []
    assert bucket_sort([0.5]) == [0.5]
