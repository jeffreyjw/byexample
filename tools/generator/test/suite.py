import unittest

from testgenerator import *
from testmochagenerator import *


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestGenerator))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestMochaGenerator))
    return test_suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    suite_test = suite()

    runner.run(suite_test)