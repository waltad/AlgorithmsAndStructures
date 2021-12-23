"""Zadanie 1: Stos
Napisz kod symulujący stos książek. Klasa powinna umożliwiać dodawanie oraz zdejmowanie książki ze stosu, przeglądanie
tytułów w stosie oraz ostatniej pozycji na stosie. Użyj magic methods umożliwiających:

dodawanie stosów do siebie
porównywanie wielkości stosów
reprezentację stringową stosu
podanie długości stosu
from typing import List

class BooksStack:
    def add_new_book(self, title: str):
        pass
    def get_book(self):
        pass
    def all_books(self) -> List[str]:
        pass
Magic methods
Klasa powinna zaimplementować następujące magic methods, aby spełnić wymagania:


def __init__(self):
    pass

def __add__(self, second_stack):
    pass

# comparision
def __gt__(self, second_stack):
    pass

def __lt__(self, second_stack):
    pass

def __ge__(self, second_stack):
    pass

def __le__(self, second_stack):
    pass

def __str__(self):
    pass

def __repr__(self):
    pass

def __len__(self):
    pass
str vs repr
Przykładowy kod wykorzystujący klasę BooksStack:


my_books = BooksStack("Mój stos książek", "Przyrodnicze")

my_books.add_new_book("Gepardy")
my_books.add_new_book("Słonie")
my_books.add_new_book("Kotki")

print(my_books.all_books())
print(my_books.get_book())
print(my_books.all_books())

her_books = BooksStack("Jej stos ksiażek", "Przyrodnicze")
her_books.add_new_book("Konie")

my_books = my_books + her_books
print(my_books.all_books())

print(my_books > her_books)
print(my_books <= her_books)

print(my_books)
print(repr(my_books))

print(len(my_books))
Oraz pożądane wyjście:


['Gepardy', 'Słonie', 'Kotki']
Kotki
['Gepardy', 'Słonie']
['Gepardy', 'Słonie', 'Konie']
True
False
Stack: Mój stos książek with category of books: Przyrodnicze
stack_name: Mój stos książek
 category: Przyrodnicze
 books: Gepardy Słonie Konie
3
"""
from typing import List, Union


class BooksStack:
    def __init__(self, stack_name: str, category: Union[None, str] = None):
        self.stack_name = stack_name
        self.category = category
        self.books: List[str] = []

    def add_new_book(self, title: str):
        self.books.append(title)

    def get_book(self) -> str:
        return self.books.pop()

    def all_books(self) -> List[str]:
        return self.books

    #  comparision
    def __add__(self, second_stack: 'BooksStack'):
        new_stack = BooksStack(stack_name=self.stack_name, category=self.category)
        new_stack.books = self.books + second_stack.books
        return new_stack

    def __gt__(self, second_stack: 'BooksStack') -> bool:
        return len(self.books) > len(second_stack.books)

    def __lt__(self, second_stack: 'BooksStack') -> bool:
        return len(self.books) < len(second_stack.books)

    def __ge__(self, second_stack: 'BooksStack') -> bool:
        return len(self.books) >= len(second_stack.books)

    def __le__(self, second_stack: 'BooksStack') -> bool:
        return len(self.books) <= len(second_stack.books)

    def __str__(self) -> str:
        return f"Stack: {self.stack_name} with category of books: {self.category}"

    def __repr__(self) -> str:
        books = ' '.join(self.books)
        return f"stack_name: {self.stack_name}\n category: {self.category}\n books: {books}"

    def __len__(self) -> int:
        return len(self.books)


if __name__ == '__main__':
    my_books = BooksStack("Mój stos książek", "Przyrodnicze")

    my_books.add_new_book("Gepardy")
    my_books.add_new_book("Słonie")
    my_books.add_new_book("Kotki")

    print(my_books.all_books())
    print(my_books.get_book())
    print(my_books.all_books())

    her_books = BooksStack("Jej stos ksiażek", "Przyrodnicze")
    her_books.add_new_book("Konie")
    print(her_books.all_books())

    my_books = my_books + her_books
    print(my_books.all_books())

    print(my_books > her_books)
    print(my_books <= her_books)

    print(my_books)
    print(repr(my_books))

    print(len(my_books))
