import unittest

from testgenerator import *
from testjasminegenerator import *


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestGenerator))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestJasmineGenerator))
    return test_suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    suite_test = suite()

    runner.run(suite_test)