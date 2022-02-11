#!/usr/local/bin/python3
# ##############################################################################
# ROT13 is a simple algorithm that shifts letters in a string forward
# 13 positions. ROT13 can be used to encrypt and decrypt strings as
# ROT13(ROT13(input)) == input.
#
# Usage: rot13 input
#
# Author : Thomas Kausch
# Date   : 10.2.2022
#
# ##############################################################################

def create_keys():
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keys = {}
    for i in range(0, 26):
        keys[lower_case[i]] = lower_case[(i + 13) % 26]
        keys[upper_case[i]] = upper_case[(i + 13) % 26]
    return keys


def encrypt(input):
    return "".join(map(lambda char: keys.get(char, char), input))


keys = create_keys()

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: rot13.py input")
        exit(1)
    print(encrypt(sys.argv[1]))
