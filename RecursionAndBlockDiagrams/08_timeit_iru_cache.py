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
from functools import lru_cache


@lru_cache(32)
def fibonacci_number_rec_cache(n: int) -> int:
    if n < 2:
        return n
    else:
        return fibonacci_number_rec_cache(n - 1) + fibonacci_number_rec_cache(n - 2)


@lru_cache(32)
def fibonacci_number_iter_cache(n: int) -> int:
    first, second = 0, 1
    if n > 1:
        for i in range(2, n + 1):
            first, second = second, first + second
    elif n >= 0:
        return n
    else:
        raise ValueError('Number should be greater than 0')
    return second


if __name__ == '__main__':
    n = 20
    print(timeit("fibonacci_number_rec(n)",
                 setup='from fibonacci_number_rec import fibonacci_number_rec; from __main__ import n', number=10))
    print(timeit("fibonacci_number_iter(n)",
                 setup='from fibonacci_number_iter import fibonacci_number_iter; from __main__ import n', number=10))

    print(timeit("fibonacci_number_rec_cache(n)",
                 setup='from __main__ import fibonacci_number_rec_cache, n', number=10))
    print(timeit("fibonacci_number_iter_cache(n)",
                 setup='from __main__ import fibonacci_number_iter_cache, n', number=10))
