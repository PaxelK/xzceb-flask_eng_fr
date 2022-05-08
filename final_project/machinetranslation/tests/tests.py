import unittest
from translator import english_to_french, french_to_english

class TestEn2Fr(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french(None), 'Input value is None')
        
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english(None), 'Input value is None')
if __name__ == '__main__':
    unittest.main()