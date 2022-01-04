"""QuickSort
Należy zaimplementować sortowanie metodą quick_sort:
[QuickSort](http://www.algorytm.edu.pl/algorytmy-maturalne/quick-sort.html
Sugestia:
W celu przypomnienia sobie rekurencji, preferowane będzie rozwiązanie zadania przy jej pomocy."""
from typing import List, Union


def quick_sort(lst: List[int], low: int = 0, high: Union[None, int] = None) -> List[int]:

    if high is None:
        high = len(lst)-1

    if low < high:
        # pi is partitioning index
        i = (low - 1)  # index of smaller element
        pivot = lst[high]  # pivot

        for j in range(low, high):

            # If current element is smaller than or
            # equal to pivot
            if lst[j] <= pivot:
                # increment index of smaller element
                i = i + 1
                lst[i], lst[j] = lst[j], lst[i]

        lst[i + 1], lst[high] = lst[high], lst[i + 1]
        pi = i + 1

        # Separately sort elements before
        # partition and after partition
        quick_sort(lst, low, pi - 1)
        quick_sort(lst, pi + 1, high)

    return lst


if __name__ == '__main__':
    data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    print(quick_sort(data))
