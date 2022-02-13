"""
 ROT13 module testing
"""
import unittest
import rot13


class TestRot13(unittest.TestCase):
    """ Testing rot13 encryption and decryption."""

    def test_invertability(self):
        """Testing invertability of rot13 encoding."""
        text = "Meet me at seven at the boat"
        self.assertEqual(rot13.encrypt(rot13.encrypt(text)), text)

    def test_lowercase_mapping(self):
        """Testing ASCII lowercase rot13 encoding."""
        text = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(rot13.encrypt(text), "nopqrstuvwxyzabcdefghijklm")

    def test_skip_utf_chars(self):
        """Testing that UTF special characgters are not encoded."""
        text = "😈😉😊😋😌"
        self.assertEqual(rot13.encrypt(text), text)

    def test_keep_punctuation_marks(self):
        """Testing that puncutation marks are not encoded."""
        text = "Keep cool!?!"
        self.assertEqual(rot13.encrypt(text)[9:], "!?!")


if __name__ == '__main__':
    unittest.main()
    unittest.main()
