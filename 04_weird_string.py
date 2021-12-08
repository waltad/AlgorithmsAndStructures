"""Zadanie 4: Dziwny string
Napisz funkcję to WeIrD CaSe, która przyjmuje stringa i zwraca go ze wszystkimi parzystymi znakami, napisanymi wielką
literą, a nieparzystymi znakami małą literą. Przyjmij indeksowanie od zera.

def to_weird_case(string: str) -> str:
    pass

Algorytm powinien działać następująco:
to_weird_case('String')
# => zwraca 'StRiNg'
to_weird_case('Algorytmy i struktury danych')
# => zwraca 'AlGoRyTmY I StRuKtUrY DaNyCh' """


def to_weird_case(string: str) -> str:
    len_string = len(string)
    new_string = ''
    for i in range(0, len_string):
        if i % 2 != 0:
            new_string += string[i].lower()
        else:
            new_string += string[i].upper()
    return new_string


if __name__ == '__main__':
    text = 'String'
    print(to_weird_case(text))
    text = 'Algorytmy i struktury danych'
    print(to_weird_case(text))

