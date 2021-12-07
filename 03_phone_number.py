"""Zadanie 3: Numer telefonu¶
Napisz funkcję, która przyjmuje listę 11 liczb całkowitych i zwraca stringa w formacie numeru telefonu.

from typing import List

def create_phone_number(n: List[int]) -> str:
    pass

Algorytm powinien działać następująco:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1])
# => returns "(+12) 345-678-901"   """
from typing import List


def create_phone_number(n: List[int]) -> str:
    return fr"(+{n[0:2]}) {n[2:5]}-{n[5:8]}-{n[8:11]}"


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]
    print(create_phone_number(numbers))
