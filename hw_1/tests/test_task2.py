import unittest

from hw_1.task2 import triplets


class TripletsTest(unittest.TestCase):
    def test_from_task(self):
        task_test_1 = ([3, 0, 1, 1, 9, 7], 7, 2, 3)
        task_test_2 = ([1, 1, 2, 2, 3], 0, 0, 1)
        self.assertEqual(triplets(*task_test_1), 4)
        self.assertEqual(triplets(*task_test_2), 0)

    def test_my_examples(self):
        self_test_1 = ([8, 5, 9, 6, 1, 3, 4], 3, 5, 9)
        self_test_2 = ([4, 9, 1, 6, 0], 4, 5, 7)
        self_test_3 = ([5, 7, 6, 0, 4, 1, 3, 8, 9, 2], 1, 2, 8)
        self_test_4 = ([8, 1, 4, 3, 0], 0, 8, 9)
        self.assertEqual(triplets(*self_test_1), 19)
        self.assertEqual(triplets(*self_test_2), 2)
        self.assertEqual(triplets(*self_test_3), 10)
        self.assertEqual(triplets(*self_test_4), 0)


if __name__ == '__main__':
    unittest.main()
