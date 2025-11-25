def counting_sort(arr: list[int]) -> list[int]:
    if not arr or len(arr) == 1:
        return arr

    lst = arr.copy()
    minn, maxx = min(lst), max(lst)
    r = maxx - minn + 1
    cntr = [0] * r

    for x in lst:
        cntr[x - minn] += 1

    i = 0
    for v, c in enumerate(cntr):
        while c > 0:
            lst[i] = v + minn
            i += 1
            c -= 1
    return lst