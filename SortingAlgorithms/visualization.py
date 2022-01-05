"""Wizualizacja
Ostatnim krokiem będzie wizualne przedstawienie osiągniętych wyników. W tym celu należy wykorzystać bibliotekę
matplotlib."""
from matplotlib import pyplot as plt

from SortingAlgorithms.auxiliary_fun_random_data import get_random_lists
from SortingAlgorithms.auxiliary_fun_times import get_times
from SortingAlgorithms.bubble_sort import bubble_sort
from SortingAlgorithms.heap_sort import heap_sort
from SortingAlgorithms.quick_sort import quick_sort


def main():
    lengths = [10, 100, 200, 300, 400, 500, 700, 800, 900, 1000]
    lsts = get_random_lists(lengths)
    quick_sort_results = get_times(lsts, quick_sort)
    bubble_sort_results = get_times(lsts, bubble_sort)
    heap_sort_results = get_times(lsts, heap_sort)
    print(quick_sort_results)
    print(bubble_sort_results)
    print(heap_sort_results)
    plt.plot(lengths, quick_sort_results, label='quick')
    plt.plot(lengths, bubble_sort_results, label='bubble')
    plt.plot(lengths, heap_sort_results, label='heap')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
