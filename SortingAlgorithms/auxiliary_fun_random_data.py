"""RandomData
Zaimplementuj funkcje generującą losowe listy z integerami. Jako wejście funkcja ta powinna przyjmować listę z
długościami docelowych list.
Przykład:
input_list = [1, 2, 4]
Następnie funkcja powinna wygenerować 3 listy: pierwsza o długości jednego elementu, druga z dwoma elementami, a trzecia
 zgodnie z dostarczonym inputem.
Na wyjściu powinna się znaleźć lista z losowymi listami (o określonej długości)
output_list = [[1], [2,5], [6,5,3,5]]
Struktura funkcji powinnna wyglądać następująco:

def get_random_lists(lengths_of_lists: List[int]) -> List[List[int]]:
    pass
"""
from random import randint
from typing import List


def get_random_lists(lengths_of_lists: List[int]) -> List[List[int]]:
    lengths_lists = []
    for length in lengths_of_lists:
        lengths_lists.append([randint(0, 100) for _ in range(length)])
    return lengths_lists


if __name__ == '__main__':
    input_list = [1, 2, 4]
    print(get_random_lists(input_list))
