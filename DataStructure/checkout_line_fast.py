"""Zadanie 2.4: Szybka kasa w sklepie
Do implementacji kolejki użycie listy nie jest optymalne, ponieważ usunięcie elementu z jej początku jest kosztowną
operacją, wymagającą przekopiowania wszystkich elementów na liście, a więc trwającą proporcjonalnie do długości listy.
W celu optymalizacji działania kolejki stwórz nową klasę, wykorzystującą typ deque dostępny w module collections. deque
posiada metody znane z listy, to znaczy append i pop. Posiada również metody popleft i appendleft. Aby uzyskać
zachowanie kolejki, należy używać metod append i popleft lub appendleft i pop.
Struktura klasy:
class FasterCashRegister(CashRegister):

    def __init__(self):
        pass

    def process(self):
        pass
"""
from DataStructure.checkout_line import CashRegister
from collections import deque

from DataStructure.line import Woman, Man, Child


class FasterCashRegister(CashRegister):

    def __init__(self):
        super().__init__()
        self.queue = deque()

    def process(self):
        client = self.queue.popleft()
        print(f"Obsługuję {client}")


if __name__ == '__main__':
    client1 = Woman("Ania", "Cebula")
    client2 = Man("John", "Smith")
    client3 = Child("Krzyś", "Nowak")

    fcr = FasterCashRegister()
    fcr.add_client(client1)
    fcr.add_client(client2)
    fcr.add_client(client3)

    fcr.process()
    fcr.process()
    fcr.process()
