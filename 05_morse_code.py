"""Zadanie 5: Kod Morsa
Chociaż obecnie Alfabet Morse’a zastąpiony jest w większości przez inne metody transmisji danych, nadal ma on swoje
zastosowanie w niektórych aplikacjach na całym świecie.

Alfabet Morse’a koduje każdy znak jako ciąg "kropek" i "kresek". Na przykład:
A = ‘·−‘
Q = ‘−−·−‘
1 = ‘·−−−−‘
W alfabecie Morse’a nie rozróżnia się wielkości liter, a tradycyjnie używa się tych dużych. Do oddzielenia kodów liter
używa się jednej spacji, a do słów 3 spacje.
HEY JUDE = ‘···· · −·−− ·−−− ··− −·· ·’
UWAGA: Dodatkowe spacje przed lub po kodzie nie mają żadnego znaczenia i powinny być ignorowane.
Oprócz liter, cyfr i znaków interpunkcyjnych, istnieją specjalne sygnały, z których najbardziej znany jest
międzynarodowy sygnał alarmowy SOS.
SOS = ‘···−−−···’
Te sygnały traktowane są jako pojedyncze znaki specjalne i zazwyczaj są przekazywane jako oddzielne słowa.
Twoim zadaniem jest zaimplementowanie funkcji, która przyjmie wyrażenie zakodowane alfabetem Morse’a jako wejście i
zwróci zdekodowany ciąg znaków, zrozumiały dla człowieka.

def decode_morse (morse_code: str) -> str:
    pass
Algorytm powinien działać następująco:

decode_morse ('.... . -.--   .--- ..- -.. .') # => 'HEY JUDE'
decode_morse(' . ') # => 'E'
decode_morse('...   ---   ...') # => 'S O S' """

MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
              '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I',
              '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
              '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S',
              '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W',
              '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1',
              '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6',
              '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?',
              '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&',
              '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
              '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}

