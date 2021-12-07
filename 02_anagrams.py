"""Zadanie 2: Anagramy¶
Napisz funkcję, która znajdzie wszystkie anagramy danego słowa z podanej listy. Znalezione wyrazy należy zwrócić
w postaci listy.

from typing import List


def anagrams(word: str, lst_of_words: List[str]) -> List[str]:
    pass
Wyjaśnienie: Czym jest anagram? Są to dwa wyrazy, które składają się z tych samych liter. Dla przykładu:

'mata' & 'tama' == true
'kat' & 'tap' == false
'meta' & 'mata' == false
'abba' & 'bbaa' == true
Podpowiedź
W zadaniu można wykorzystać Counter"""
from collections import Counter
from typing import List


def anagrams(word: str, lst_of_words: List[str]) -> List[str]:
    anagram_lst = []
    for x in lst_of_words:
        if Counter(word) == Counter(x):
            anagram_lst.append(x)
    return anagram_lst


if __name__ == '__main__':
    lst_word = ['tama', 'tratata', 'atma', 'atam', 'mama', 'maat', 'taam', 'gol']
    print(anagrams('mata', lst_word))
