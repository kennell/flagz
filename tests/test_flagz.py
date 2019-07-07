import unittest
import flagz


class TestFlagz(unittest.TestCase):

    def test_get_by_code_lowercase(self):
        flag = flagz.get_by_code('de')
        self.assertEqual(flag, '🇩🇪')

    def test_get_by_code_uppercase(self):
        flag = flagz.get_by_code('DE')
        self.assertEqual(flag, '🇩🇪')

    def test_get_by_code_invalid(self):
        with self.assertRaises(ValueError):
            flagz.get_by_code('xx')
