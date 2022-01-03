"""BubbleSort
Należy stworzyć funkcję implementującą działanie algorytmu bubblesort.
Sortowanie bąbelkowe jest bardzo łatwe - sprawdzamy czy następny element tablicy jest większy od aktualnego, jeżeli tak,
to zamieniamy te elementy miejscami.
Struktura funkcji powinnna wyglądać następująco:

def bubble_sort(lst: List[int]) -> List[int]:
    pass
"""
from typing import List


def bubble_sort(lst: List[int]) -> List[int]:
    n = len(lst)
    while n > 1:
        for i in range(0, n-1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n -= 1
    return lst


def bubble_sort2(lst: List[int]) -> List[int]:
    # We go through the list as many times as there are elements
    for i in range(len(lst)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


if __name__ == '__main__':
    l = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(bubble_sort(l))
    l = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(bubble_sort2(l))
