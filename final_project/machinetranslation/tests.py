import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench("Hello"), "Bonjour") 
        self.assertEqual(englishToFrench(null), null) 
        self.assertNotEqual(englishToFrench("welcome"), "welcome")  

    def test2(self): 
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello") 
        self.assertEqual(frenchToEnglish(null), null)
        self.assertNotEqual(frenchToEnglish("Bienvenue"), "Bienvenue") 

unittest.main()