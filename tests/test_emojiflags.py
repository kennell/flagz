import unittest
import emojiflags


class TestEmojiflags(unittest.TestCase):

    def test_get_by_code_lowercase(self):
        flag = emojiflags.get_by_code('de')
        self.assertEqual(flag, '🇩🇪')

    def test_get_by_code_uppercase(self):
        flag = emojiflags.get_by_code('DE')
        self.assertEqual(flag, '🇩🇪')

    def test_get_by_code_invalid(self):
        with self.assertRaises(ValueError):
            emojiflags.get_by_code('xx')
