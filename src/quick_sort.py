def quick_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    elem = arr[len(arr) // 2]
    left = [x for x in arr if x < elem]
    mid = [x for x in arr if x == elem]
    right = [x for x in arr if x > elem]
    return quick_sort(left) + mid + quick_sort(right)
