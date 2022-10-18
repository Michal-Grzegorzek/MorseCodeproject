MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}



def encrypt(string):
    lst = []
    lst.extend(string.upper())
    string_after_convert = ''
    for a in range(len(lst)):
        for i in MORSE_CODE_DICT:
            if i == lst[a]:
                string_after_convert = f'{string_after_convert}{MORSE_CODE_DICT[i]} '

    print(string_after_convert)


def decrypt(string):
    lst = []
    lst.extend(string)
    string_after_split = string.split()
    string_after_convert = ''
    for a in range(len(string_after_split)):
        for i in MORSE_CODE_DICT:
            if MORSE_CODE_DICT[i] == string_after_split[a]:
                string_after_convert = f'{string_after_convert}{i}'

    print(string_after_convert)


while(True):
    answer = input("Enter number 1 if you want encrypt message, enter number 2 if you want "
                   "decrypt message, enter number 0 if you want to quit:")

    if answer == '0':
        break

    message = input("Enter a message:")

    if answer == '1':
        encrypt(message)

    if answer == '2':
        decrypt(message)
