import unittest
from tools.generator.src.mochagenerator import *


class TestMochaGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = MochaGenerator()

    def test_report(self):
        self.assertEqual(self.generator.report(), {"key":"value"})

if __name__ == "__main__":
    unittest.main()
