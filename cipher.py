import sys,random

print("This program is written by futureTech. It's is mostly \napplicable in minitary field where it is used to pass secret message.")
print('Welcome to the land of security. It matters to secured')

LETTER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

encodeddict = {

        'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4,

        'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8,

        'i' : 9, 'j' : 10, 'k' : 11, 'l' : 12,

        'm' : 13, 'n' : 14, 'o' : 15, 'p' : 16,

        'q' : 17, 'r' : 18, 's' : 19, 't' : 20,

        'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24,

        'y' : 25, 'z' :26, ' ' : 100, 'A' : 101,

        'B' : 102, 'C' : 103, 'D' : 103, 'E' : 104,

        'F' : 105, 'G' : 106, 'H' : 107, 'I' : 108,

        'J' : 109, 'K' : 110, 'L' : 111, 'M' : 112,

        'N' : 113, 'O' : 114, 'P' : 115, 'Q' : 116,

        'R' : 117, 'S' : 118, 'T' : 119, 'U' : 120,

        'V' : 121, 'W' : 122, 'X' : 123, 'Y' : 124,

        'Z' : 125, '.' : 200, '/' : 201, '\\' : 202,

        '$' : 203, '#' : 204, '@' : 205, '%' : 206,

        '^' : 207, '*' : 208, '(' : 209, ')' : 210,

        '_' : 211, '-' : 212, '=' : 213, '+' : 214,

        '>' : 215, '<' : 216, '?' : 217, ';' : 218,

        ':' : 219, '\'' : 220, '\"' : 221, '{' : 222,

        '}' : 223, '[' : 224, ']' : 225, '|' : 226,

        '`' : 227, '~' : 228, '!' : 229, '0' : 300,

        '1' : 301, '2' : 302, '3' : 303, '4' : 304,

        '5' : 306, '6' : 307, '7' : 308, '8' : 309,

        '9' : 310
}


def encrypt_message(message,key):
    translated = ' '
    for i in message:
        if i in LETTER:
            return NULL

    


while 1:
    print('Please do you want to (e)ncrpt or (d)ecrypt?')
    response = input('> ').lower()

    if response.startswith('e'):
        mode = 'enccrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print("Please enter 'e' or 'd'")

# Let's get the key from the user
while 1:
    print('Please specify the key to use')
    print(' It can be a letter of combination of letters')
    response = input('> ').upper()

    if response.isalpha():
        key = response
    print("not yet done with this brach of code")

    break
#Let's get the message from the user

print('Please enter the message to be worked on')
response = input('> ')




