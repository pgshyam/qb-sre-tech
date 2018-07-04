import unittest
import test_generate

#initialize
loader = unittest.TestLoader()
suite = unittest.TestSuite()

#add tests
suite.addTests(loader.loadTestsFromModule(test_generate))

# run the suite
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)