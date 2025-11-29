from typing import Callable
import time


def timeit_once(func: Callable, *args, **kwargs) -> float:
    """
    Замер одного вызова, возвращает время в секундах.
    """
    start = time.perf_counter()
    func(*args, **kwargs)
    end = time.perf_counter()
    return end - start


def benchmark_sorts(arrays: dict[str, list[int]], algos: dict[str, Callable[[list[int]], list[int]]]) -> dict[str, dict[str, float]]:
    """
    Бенчмарк сортировок, возвращает времена по массивам.
    """
    results: dict[str, dict[str, float]] = {}
    # по типам массивов
    for arr_name, arr in arrays.items():
        results[arr_name] = {}
        # по алгоритмам
        for algo_name, algo in algos.items():
            # копия массива
            t = timeit_once(algo, arr.copy())
            results[arr_name][algo_name] = t
    return results
