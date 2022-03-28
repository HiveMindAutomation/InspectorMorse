import json
import string


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

def encrypt(message):

    # list comprehension to convert input String to a list.
    character_list = [char for char in message.upper()]
    # convert input to morse code list
    morse = ''
    for char in character_list:
        if char == ' ':
            morse += ' '
        else:
            morse += MORSE_CODE_DICT[char] + ' '

    print(morse)

def decrypt(message):
    character_list = message.split(' ')
    # print(character_list)
    # convert morse code to english list
    output = []
    for char in character_list:
        if char == '':
            output += ' '
        else:
            output += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(char)]
    output = ' '.join([str(elem) for elem in output])
    print(output)

function = 0

while function not in [1,2]:
    function = int(input('Choose your function\n1) to encrypt:\n2) to decrypt:\n3) quit:\n'))

    if function == 1:
        string_to_convert = input("Enter the string you want to convert to Morse Code:\n")
        encrypt(string_to_convert)
        function = 0
    elif function == 2:
        string_to_convert = input("Enter the Morse Code you want to convert back to English:\n")
        decrypt(string_to_convert)
        function = 0
    elif function == 3:
        exit()