import unittest
import rot13


class TestRot13(unittest.TestCase):

    def test_invertability(self):
        text = "Meet me at seven at the boat"
        self.assertEqual(rot13.encrypt(rot13.encrypt(text)), text)

    def test_lowercase_mapping(self):
        text = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(rot13.encrypt(text), "nopqrstuvwxyzabcdefghijklm")

    def test_skip_utf_chars(self):
        text = "😈😉😊😋😌"
        self.assertEqual(rot13.encrypt(text), text)

    def test_keep_punctuation_marks(self):
        text = "Keep cool!?!"
        self.assertEqual(rot13.encrypt(text)[9:], "!?!")


if __name__ == '__main__':
    unittest.main()
    unittest.main()
