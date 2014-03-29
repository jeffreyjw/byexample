import unittest
from tools.generator.src.generator import *


class TestGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = Generator()

    def test_report(self):
        self.assertEqual(self.generator.report(), {"key":"value"})

if __name__ == "__main__":
    unittest.main()
