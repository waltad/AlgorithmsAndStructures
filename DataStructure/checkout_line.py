"""Zadanie 2.3: Kasa w sklepie
Zaimplementuj instancję klasy będącej symulacją działania sklepu. Kasa powinna posiadać kolejkę oraz mieć możliwość
dołączania nowych klientów do niej, jak i obsługiwania ich. Wykorzystaj zaimplementowaną klasę kolejki FIFO.

class CashRegister:
    def add_client(self, client: Client):
        pass
    def process(self) -> Client:
        pass
Przykładowe dane do zadania:

client1 = Woman("Ania", "Cebula")
client2 = Man("John", "Smith")
client3 = Child("Krzyś", "Nowak")

cr = CashRegister()
cr.add_client(client1)
cr.add_client(client2)
cr.add_client(client3)

cr.process()
cr.process()
cr.process()
"""
from line import Client, Woman, Man, Child


class CashRegister:
    def add_client(self, client: Client):
        pass

    def process(self) -> Client:
        pass
