"""Times
Druga funckcja pomocnicza ma za zadanie pobieranie listy. Funkcji, która na tej liście będzie wywoływana i zwracanie
 czasu trwania tej funkcji.
Struktura funkcji powinnna wyglądać następująco:

 def get_times(
    lists: List[List[int]],
    sort_function: Callable[[List[int]],
    List[int]])
        -> List[float]:
    pass
Wyjaśnienie:
Poprzez Callable informuje się o argumencie będącym funcją. W nawiasach kwadratowych dodatkowo znajduje się informacja
co i na co przetwarzane jest za jej pomocą.
"""
import copy
import time
from typing import List, Callable

from SortingAlgorithms.auxiliary_fun_random_data import get_random_lists
from SortingAlgorithms.bubble_sort import bubble_sort


def get_times(
        lists: List[List[int]],
        sort_function: Callable[[List[int]], List[int]]
) -> List[float]:
    temp_lists = copy.deepcopy(lists)
    times = []
    for temp_list in temp_lists:
        start = time.time()
        sort_function(temp_list)
        end = time.time()
        times.append(end - start)
    return times


if __name__ == '__main__':
    input_list = [100, 1000, 2000]
    random_lists = get_random_lists(input_list)
    print(get_times(random_lists, bubble_sort))
