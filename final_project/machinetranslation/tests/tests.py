import unittest
import translator

class TestEF(unittest.TestCase):
    def runTest(self):
        self.assertEqual(translator.english_to_french(
            None), "", "False")
        self.assertEqual(translator.english_to_french('Hello'),
                         "Bonjour", "False")

class TestFE(unittest.TestCase):
    def runTest(self):
        self.assertEqual(translator.french_to_english(None), "", "False")
        self.assertEqual(translator.french_to_english("Bonjour"), "Hello", "False")

unittest.main()
