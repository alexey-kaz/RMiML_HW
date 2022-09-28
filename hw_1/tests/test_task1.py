import unittest

from hw_1.task1 import balanced_brackets


class BracketsTest(unittest.TestCase):
    def test_hello(self):
        task_test_1 = "(hello)"
        self.assertEqual(balanced_brackets(task_test_1), True)

    def test_switch_bracket(self):
        task_test_2 = "(22+3)*(21/[34+1)]"
        self.assertEqual(balanced_brackets(task_test_2), False)

    def test_many_correct(self):
        self_test_1 = "[()]{}{[(){}()]()}"
        self.assertEqual(balanced_brackets(self_test_1), True)

    def test_no_brackets(self):
        self_test_2 = "123"
        self.assertEqual(balanced_brackets(self_test_2), True)

    def test_many_incorrect(self):
        self_test_3 = "{}[(}{}])({})"
        self.assertEqual(balanced_brackets(self_test_3), False)


if __name__ == '__main__':
    unittest.main()
