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
from DataStructure.queue_fifo import FifoList
from DataStructure.line import Client, Woman, Man, Child


class CashRegister:
    def __init__(self):
        self.queue = FifoList()

    def add_client(self, client: Client):
        self.queue.append(client)
        print(f"{client} dołączył do koleji")

    def process(self) -> Client:
        client = self.queue.pop()
        print(f"Obsługuję {client}")

    # def all_clients(self):
    #     for client in self.queue:
    #         print(client, end=', ')
    #     print()


if __name__ == '__main__':
    client1 = Woman("Ania", "Cebula")
    client2 = Man("John", "Smith")
    client3 = Child("Krzyś", "Nowak")

    cr = CashRegister()
    cr.add_client(client1)
    cr.add_client(client2)
    cr.add_client(client3)

    # cr.all_clients()

    cr.process()
    cr.process()
    cr.process()
