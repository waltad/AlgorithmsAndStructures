"""Zadanie 1: Schemat blokowy
Zaimplementuj algorytm zaprezentowany na następującym schemacie blokowym:

Flowchart

Podpowiedź
Algorytm ten to tzn. Binary Search. Służy on do znajdowania miejsca poszukiwanego elementu w liście.
Więcej informacji można znaleźć pod poniższym linkiem:
http://www.algorytm.edu.pl/algorytmy-maturalne/wyszukiwanie-binarne.html

Przykładowe użycie:

# Test array
test_lst = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binary_search_iter(test_lst, x)

if result != -1:
    print("Element is present at index {}".format(result))
else:
    print("Element is not present in array") """
from typing import List


def binary_search_iter(lst: List, key: int) -> int:
    start = 0
    end = len(lst) - 1

    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == key:
            return "Element is present at index {}".format(mid)
        if lst[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return "Element is not present in array"


if __name__ == '__main__':
    test_lst = [2, 3, 4, 10, 40]
    x = 10
    print(binary_search_iter(test_lst, x))



