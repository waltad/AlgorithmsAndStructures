"""Ciąg Fibonacciego
Kolejne wyrazy tego ciągu tworzonone są przez dodanie do siebie dwóch poprzednich. Przy założeniu, że pierwszy wyraz = 0,
a drugi = 1:
Ciąg Fibonacciego: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89…

Zadanie 6: Fibonacci iteracyjnie
Napisz w Pythonie implementacje iteracyjnego obliczania n-tego wyrazu ciągu Fibonacciego

Wyjaśnienie:
first_number, second_number = second_number, first_number
W wielu językach programowania, żeby zamienić miejscami dwie wartości, musimy wykorzystać w tym celu tymczasową zmienną.
Dzięki systemowi "odpakowywania" w Pythonie możemy zastosować powyższy trick.
Więcej na ten temat można przeczytać: https://riptutorial.com/python/example/2845/unpacking-iterables """


def fibonacci_number_iter(n: int) -> int:
    first, second = 0, 1
    if n > 1:
        for i in range(2, n+1):
            first, second = second, first + second
    elif n >= 0:
        return n
    else:
        raise ValueError('Number should be greater than 0')
    return second


if __name__ == '__main__':
    x = 12
    print(fibonacci_number_iter(x))
