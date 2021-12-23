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
        self.list: List = []

    def append(self, data):
        self.list.append(data)

    def pop(self):
        self.list.pop(0)
