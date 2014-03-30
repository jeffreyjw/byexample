import unittest
from tools.generator.src.jasminegenerator import *


class TestJasmineGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = JasmineGenerator()

    def test_report(self):
        self.assertEqual(self.generator.report(), {"key":"value"})

if __name__ == "__main__":
    unittest.main()
