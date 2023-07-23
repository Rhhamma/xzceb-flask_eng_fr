import unittest
from translator import french_to_english , english_to_french

class TestEnglishToFrench(unittest.TestCase):
    def test(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertEqual(english_to_french('Bread'),'Pain')
        

class TestFrenchToEnglish(unittest.TestCase):
    def test(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertEqual(french_to_english('pain'),'bread')
        

unittest.main()
