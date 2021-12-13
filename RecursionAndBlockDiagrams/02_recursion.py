"""Zadanie 2: Rekurencja!
Zaimplementuj powyższy algorytm z wykorzystaniem rekurencji.

W ramach wyjaśnienia poniższego fragmentu kodu:

from typing import List
def binary_search_rec(lst: List[int], key: int, start: int = 0, end: int = None):
    pass
Programowanie ma to do siebie i charakteryzuje się tym, że dłużej i częściej kod się "czyta", a nie pisze. Im bardziej
nasz kod będzie klarowny i zrozumiały dla czytelnika, tym lepiej. W tym celu warto stosować typowanie, które sugeruje,
jakiego typu są poszczególne zmienne.

Silnia
Silnia z n to iloczyn wszystkich liczb naturalnych nie większych od n.
n! = n x (n−1) x (n−2) x (n−3) ⋅⋅⋅⋅ x 3 x 2 x 1
Powyższe wyrażenie możemy jednak zapisać rekurencyjnie:
n! = n x (n−1)!
n! = n x (n−1) x (n-2)!
Jeżeli liczba jest mniejsza od 2 zwróć 1. W przeciwnym wpadku zwróć liczba razy silnia(liczba-1)"""

