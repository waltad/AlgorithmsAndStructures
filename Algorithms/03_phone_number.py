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
    n = [str(figure) for figure in n]
    return fr"(+{''.join(n[0:2])}) {''.join(n[2:5])}-{''.join(n[5:8])}-{''.join(n[8:11])}"


def create_phone_number2(n: List[int]) -> str:
    str1 = ''.join(str(x) for x in n[0:2])
    str2 = ''.join(str(x) for x in n[2:5])
    str3 = ''.join(str(x) for x in n[5:8])
    str4 = ''.join(str(x) for x in n[8:11])

    return '(+{}) {}-{}-{}'.format(str1, str2, str3, str4)


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]
    print(create_phone_number(numbers))
    print(create_phone_number2(numbers))
