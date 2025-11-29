def counting_sort(arr: list[int]) -> list[int]:
    """
    Подсчётная сортировка.
    Для целых в диапазоне.
    """
    if not arr or len(arr) == 1:
        return arr

    lst = arr.copy()   # копия входа
    minn, maxx = min(lst), max(lst)   # границы
    r = maxx - minn + 1   # длина диапазона
    cntr = [0] * r    # счётчик

    for x in lst:
        cntr[x - minn] += 1
    i = 0

    # восстановление
    for v, c in enumerate(cntr):
        while c > 0:
            lst[i] = v + minn
            i += 1
            c -= 1
    return lst    # отсортированный список
