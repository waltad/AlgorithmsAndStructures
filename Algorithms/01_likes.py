"""Zadanie 1: Lajki!
Zaimplementuj system poprawnego wyświetlania ilości „lajków” znany z Facebooka.
Wyjaśnienie: Funkcja likes powinna przyjmować na wejściu listę stringów, zawierającą imiona osób, które „lubią” dany
wpis/zdjęcie, a na wyjściu dawać odpowiednio sformatowany tekst.

from typing import List

def likes(names: List[str]) -> str:
    pass 
Ostatecznie algorytm powinien działać następująco:

likes([]) # => "nikt tego nie lubi"
likes(["Piotr"]) # => "Piotr lubi to!"
likes(["Piotr", "Ania"]) # => "Piotr i Ania lubią to"
likes(["Piotr", "Ania", "Marek"]) # => "Piotr, Ania i Marek lubią to"
likes(["Piotr", "Ania", "Marek", "Ola"]) # => "Piotr, Ania i 2 inne osoby lubią to"""

from typing import List


def likes(names: List[str]) -> str:
    num_of_names = len(names)
    output = ""
    if num_of_names == 0:
        output = "nikt tego nie lubi :("
    elif num_of_names == 1:
        output = f"{names[0]} lubi to!"
    elif num_of_names == 2:
        output = f"{names[0]} i {names[1]} lubią to."
    elif num_of_names == 3:
        output = f"{names[0]}, {names[1]} i {names[2]} lubią to."
    elif num_of_names >= 4:
        output = f"{names[0]}, {names[1]} i {num_of_names - 2} inne osoby lubią to."

    return output


if __name__ == '__main__':
    print(likes([]))
    print(likes(["Piotr"]))
    print(likes(["Piotr", "Ania"]))
    print(likes(["Piotr", "Ania", "Marek"]))
    print(likes(["Piotr", "Ania", "Marek", "Ola"]))
