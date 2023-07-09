import unittest
from translator import french_to_english , english_to_french

class TestTranslator(unittest.TestCase):
        def test_englishToFrench(self):
            self.assertEqual(french_to_english('Bonjour'),'Hello')
        
        def test_frenchToEnglish(self):
            self.assertEqual(english_to_french('Hello'),'Bonjour')

if __name__ == "__main__":
    unittest.main()