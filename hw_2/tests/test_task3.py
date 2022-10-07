import unittest

from hw_2.task3 import network_delay

test_1 = ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2)
test_2 = ([[1, 2, 1]], 2, 2)
test_3 = ([[1, 2, 1], [2, 3, 7], [1, 3, 4], [2, 1, 2]], 3, 2)
test_4 = ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 3)
test_5 = ([[1, 2, 1]], 2, 1)
test_6 = ([[1, 2, 1], [2, 3, 7], [1, 3, 4], [2, 1, 2]], 4, 1)


class NetworkDelayTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(network_delay(*test_1), 2)

    def test_2(self):
        self.assertEqual(network_delay(*test_2), -1)

    def test_3(self):
        self.assertEqual(network_delay(*test_3), 6)

    def test_4(self):
        self.assertEqual(network_delay(*test_4), -1)

    def test_5(self):
        self.assertEqual(network_delay(*test_5), 1)

    def test_6(self):
        self.assertEqual(network_delay(*test_6), -1)


if __name__ == '__main__':
    unittest.main()
