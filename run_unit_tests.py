import unittest
import test.test_utils as testcase

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(testcase))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)