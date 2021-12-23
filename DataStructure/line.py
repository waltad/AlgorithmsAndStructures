"""Zadanie 2: Symulacja kolejki
Zadanie 2.1: Klienci
Zaimplementuj abstrakcyjną klasę Klienta sklepu oraz 3 klasy dziedziczące po niej. Wyróżniamy 3 grupy klientów:
Kobiety
Mężczyźni
Dzieci
Do każdej z tych grup należy zwracać się w inny sposób, kobiety per Pani, meżczyźni per Pan, a zwracając się do dzieci
nie należy stosować przedrostka.

Podpowiedź
Każda klasa dziedzicząca powinna mieć własną reprezentację stringową"""

import abc


class Client(abc.ABC):
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @abc.abstractmethod
    def __str__(self) -> str:
        pass


class Woman(Client):
    def __str__(self) -> str:
        return f"Miss {self.first_name} {self.last_name}"


class Man(Client):
    def __str__(self) -> str:
        return f"Mister {self.first_name} {self.last_name}"


class Child(Client):
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
