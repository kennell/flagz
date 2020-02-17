import unittest
import flagz


class TestFlagz(unittest.TestCase):

    def test_by_code_lowercase(self):
        flag = flagz.by_code('de')
        self.assertEqual(flag, '🇩🇪')

    def test_by_code_uppercase(self):
        flag = flagz.by_code('DE')
        self.assertEqual(flag, '🇩🇪')
