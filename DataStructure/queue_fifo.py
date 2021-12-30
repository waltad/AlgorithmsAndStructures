"""Zadanie 2.2: Kolejka FIFO
Kolejka FIFO
Podczas gdy w przypadku stosu ostatni dodany element jest pierwszym, który opuści stos, w kolejce jest inaczej: pierwszy
dodany element opuści ją też jako pierwszy. Jest to zasada First In, First Out (FIFO).

Zadanie polega na stworzeniu klasy kolejki za pomocą listy. W tym celu dodawanie elementu powinno polegać na
wykorzystaniu metody append (dodanie obiektu na koniec kolejki) Natomiast usunięcie elementu powinno być zrealizowanie
przez usuwanie pierwszego elementu listy z wykorzystaniem pop (opuszczenie kolejki przez obiekt na jej początku)

Struktura klasy:
class FifoList:
    def __init__(self):
        pass

    def append(self, data):
        pass

    def pop(self):
        pass
"""
from typing import List


class FifoList:
    def __init__(self):
        self.data: List = []

    def append(self, data):
        self.data.append(data)

    def pop(self):
        return self.data.pop(0)


if __name__ == '__main__':
    new_list = FifoList()
    new_list.append('Luck')
    new_list.append('Batman')
    new_list.append('Spider-man')

    print(new_list.data)

    print(new_list.pop())
    print(new_list.pop())
    print(new_list.pop())
