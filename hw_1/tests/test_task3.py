import unittest

from hw_1.task3 import top_k_n, top_k_nlogn

task_test_1 = ([1, 1, 1, 2, 2, 3], 2)
task_test_2 = ([1], 1)
self_test_1 = ([1, 1, 1, 2, 2, 3, 3], 2)
self_test_2 = ([1, 1, 1, 2, 2, 3, 3, 3], 2)
self_test_3 = ([1, 1, 1, 2, 2, 3, 3, 3, 4], 3)
self_test_4 = ([1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4], 2)


class NLogNComplexity(unittest.TestCase):
    def test_from_task(self):
        self.assertEqual(top_k_nlogn(*task_test_1), [1, 2])
        self.assertEqual(top_k_nlogn(*task_test_2), [1])

    def test_order_1(self):
        self.assertEqual(top_k_nlogn(*self_test_1), [1, 2])

    def test_order_2(self):
        self.assertEqual(top_k_nlogn(*self_test_2), [1, 3])

    def test_more_terms_order(self):
        self.assertEqual(top_k_nlogn(*self_test_3), [1, 3, 2])

    def test_count(self):
        self.assertEqual(top_k_nlogn(*self_test_4), [1, 3])


class NComplexity(unittest.TestCase):
    def test_from_task(self):
        self.assertEqual(top_k_n(*task_test_1), [1, 2])
        self.assertEqual(top_k_n(*task_test_2), [1])

    def test_order_1(self):
        self.assertEqual(top_k_nlogn(*self_test_1), [1, 2])

    def test_order_2(self):
        self.assertEqual(top_k_nlogn(*self_test_2), [1, 3])

    def test_more_terms_order(self):
        self.assertEqual(top_k_nlogn(*self_test_3), [1, 3, 2])

    def test_count(self):
        self.assertEqual(top_k_nlogn(*self_test_4), [1, 3])


if __name__ == '__main__':
    unittest.main()
