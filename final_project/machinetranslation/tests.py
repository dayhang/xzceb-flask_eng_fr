import unittest
import translator

class TestE2FTranslator(unittest.TestCase):
    def runTest(self):
        self.assertEqual(translator.englishToFrench(
            None), "", "failed to translate correct")
        self.assertEqual(translator.englishToFrench('Hello'),
                         "Bonjour", "failed to translate correct")


class TestF2ETranslator(unittest.TestCase):
    def runTest(self):
        self.assertEqual(translator.frenchToEnglish(
            None), "", "failed to translate correct")
        self.assertEqual(translator.frenchToEnglish("Bonjour"),
                         "Hello", "failed to translate correct")


unittest.main()
