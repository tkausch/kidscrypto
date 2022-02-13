#!/usr/local/bin/python3
"""
 ROT13 is a simple algorithm that shifts letters in a string forward
 13 positions.

 ROT13 can be used to encrypt and decrypt strings.
"""


def setup_key_map(key_mapping):
    """Create encryption and decryption dictionary. """

    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(0, 26):
        key_mapping[lower_case[i]] = lower_case[(i + 13) % 26]
        key_mapping[upper_case[i]] = upper_case[(i + 13) % 26]


def encrypt(text):
    """Return the rot13 encoded input string."""
    return "".join(map(lambda char: key_map.get(char, char), text))


key_map = {}
setup_key_map(key_map)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: rot13.py input")
        sys.exit(1)
    print(encrypt(sys.argv[1]))
