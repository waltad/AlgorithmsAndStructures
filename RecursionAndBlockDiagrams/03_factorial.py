"""Silnia
Silnia z n to iloczyn wszystkich liczb naturalnych nie większych od n.
n! = n x (n−1) x (n−2) x (n−3) ⋅⋅⋅⋅ x 3 x 2 x 1
Powyższe wyrażenie możemy jednak zapisać rekurencyjnie:
n! = n x (n−1)!
n! = n x (n−1) x (n-2)!
Jeżeli liczba jest mniejsza od 2 zwróć 1. W przeciwnym wpadku zwróć liczba razy silnia(liczba-1)
Zadanie 3: Silnia - schematy blokowe
Przedstaw algorytm obliczania silni z podanej liczby w postaci schematu blokowego. Stwórz rozwiązanie działające
iteracyjnie, jak i takie oparte na rekurencji."""


def factorial_iter(n: int):
    result = 1
    if n in (0, 1):
        return 1
    elif n > 1:
        for i in range(1, n + 1):
            result = result * i
    else:
        raise ValueError('Number should be greater than 0')
    return result


if __name__ == '__main__':
    x = 5
    print(factorial_iter(x))
