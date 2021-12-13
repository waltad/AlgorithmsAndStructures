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


def decode_morse(morse_code: str) -> str:
    encode_words_list = morse_code.split('   ')
    words_list = []
    for encode_word in encode_words_list:
        list_signs = encode_word.split(' ')
        word = ''
        for sign in list_signs:
            word += MORSE_CODE.get(sign, '')
        if word:
            words_list.append(word)

    return ' '.join(words_list)


def decode_morse2(morse_sequence: str)-> str:
    words = []
    for morse_word in morse_sequence.split('   '):
        word = ''.join(MORSE_CODE.get(morse_char, '') for morse_char in morse_word.split(' '))
        if word:
            words.append(word)
    return ' '.join(words)


if __name__ == '__main__':
    morse_code1 = '.... . -.--   .--- ..- -.. .'  # => 'HEY JUDE'
    morse_code2 = ' . '  # => 'E'
    morse_code3 = '...   ---   ...'  # => 'S O S'
    print(decode_morse(morse_code1))
    print(decode_morse(morse_code2))
    print(decode_morse(morse_code3))
    print(decode_morse2(morse_code1))
    print(decode_morse2(morse_code2))
    print(decode_morse2(morse_code3))
