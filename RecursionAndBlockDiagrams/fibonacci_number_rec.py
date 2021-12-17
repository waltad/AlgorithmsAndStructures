"""Zadanie 7: Fibonacci rekurencyjnie
Napisz w Pythonie implementacje rekurencyjnego liczenia n-tego wyrazu ciągu Fibonacciego."""


def fibonacci_number_rec(n: int) -> int:
    if n < 2:
        return 0
    elif n < 3:
        return 1
    else:
        return fibonacci_number_rec(n - 2) + fibonacci_number_rec(n - 1)


if __name__ == '__main__':
    x = 12
    print(fibonacci_number_rec(x))
