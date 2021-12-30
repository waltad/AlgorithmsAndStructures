"""Zadanie 2.5 Porównaj czas działania¶
Porównaj szybkość działania obu podejść."""
from datetime import timedelta
from time import time
from timeit import timeit
from DataStructure.line import Woman, Man, Child
from checkout_line import CashRegister
from checkout_line_fast import FasterCashRegister

if __name__ == '__main__':
    client1 = Woman("Ania", "Cebula")
    client2 = Man("John", "Smith")
    client3 = Child("Krzyś", "Nowak")

    cr = CashRegister()
    cr.add_client(client1)
    cr.add_client(client2)
    cr.add_client(client3)

    fcr = FasterCashRegister()
    fcr.add_client(client1)
    fcr.add_client(client2)
    fcr.add_client(client3)

    print(timeit('cr.process', setup='from DataStructure.line import Woman, Man, Child;'
                                     ' from checkout_line import CashRegister; from __main__ import cr'))
    print(timeit('fcr.process', setup='from DataStructure.line import Woman, Man, Child;'
                                     ' from checkout_line_fast import FasterCashRegister; from __main__ import fcr'))

    start = time()

    cr = CashRegister()
    for i in range(10000):
        cr.add_client(client1)
    for i in range(10000):
        cr.process()
        duration = time() - start

    start = time()

    cr = FasterCashRegister()
    for i in range(10000):
        cr.add_client(client1)
    for i in range(10000):
        cr.process()
        duration2 = time() - start

    print(duration)
    print(duration2)
