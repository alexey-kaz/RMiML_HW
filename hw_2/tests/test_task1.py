import unittest

from hw_2.task1 import MedianFinder


class MedianTest(unittest.TestCase):
    def test_blank(self):
        median_finder = MedianFinder()
        self.assertEqual(median_finder.find_median(), .0)

    def test_single(self):
        median_finder = MedianFinder()
        median_finder.add_num(1)
        self.assertEqual(median_finder.find_median(), 1)

    def test_even_length(self):
        median_finder = MedianFinder()
        median_finder.add_num(1)
        median_finder.add_num(2)
        self.assertEqual(median_finder.find_median(), 1.5)

    def test_odd_length(self):
        median_finder = MedianFinder()
        median_finder.add_num(1)
        median_finder.add_num(2)
        median_finder.add_num(3)
        self.assertEqual(median_finder.find_median(), 2)


if __name__ == '__main__':
    unittest.main()
