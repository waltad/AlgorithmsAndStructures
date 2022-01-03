"""HeapSort
Należy zaimplementować metode sortowania heapsort:
HeapSort
W tym celu należy skorzystać z poniższej biblioteki heapq.
Sugestia:
Za pomocą Python tutor warto zobaczyć w jaki sposób przetwarzany jest kopiec"""

from heapq import heappop, heappush
from typing import List


def heap_sort(lst: List[int]) -> List[int]:
    heap = []
    sort_lst = []
    for element in lst:
        heappush(heap, element)

    while heap:
        sort_lst.append(heappop(heap))

    return sort_lst


def heap_sort2(lst: List[int]) -> List[int]:
    h = []
    for value in lst:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]


if __name__ == '__main__':
    data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    print(heap_sort(data))
    print(heap_sort2(data))


