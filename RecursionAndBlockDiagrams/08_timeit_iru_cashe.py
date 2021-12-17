"""Zadanie 8: timeit i lru_cache
Porównaj ze sobą oba algorytmy umożlwiające obliczenie n-tego wyrazu ciągu Fibonacciego. Któremu z nich rozwiązanie
zajmuje dłużej? W celu realizacji zadania wykorzystaj bibliotekę timeit

Ciekawym rozwiązanie jest zastosowanie dekoratora lru_cache, umożliwia on "zapamiętywanie" w pamięci ostatnich wyników.
Dzięki temu nie ma potrzeby ponownego ich obliczania.

Wykorzystując lru_cache postaraj się przyspieszyć działanie tych algorytmów. Porównaj czas wykonywania się
poszczególnych funkcji za pomocą timeit.

Nie są to oczywiście jedyne "sztuczki", które mogą sprawdzić, że Python wcale nie będzie taki wolny. Inne sposoby
zostały opisane w poniższym artykule, przy okazji porównania języka Python z Julią:
https://towardsdatascience.com/how-to-make-python-faster-than-julia-b2c621130ae2 """
from timeit import timeit


if __name__ == '__main__':
    n = 20
    print(timeit("fibonacci_number_rec(n)",
                 setup='from fibonacci_number_rec import fibonacci_number_rec; from __main__ import n', number=10))
    print(timeit("fibonacci_number_iter(n)",
                 setup='from fibonacci_number_iter import fibonacci_number_iter; from __main__ import n', number=10))
