import unittest

loader = unittest.TestLoader()
start_dir = 'tests'
suite = loader.discover(start_dir)

runner = unittest.TextTestRunner(verbosity=2)

if __name__ == '__main__':
    runner.run(suite)
