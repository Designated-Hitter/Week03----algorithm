import Q1700_SHC
from unittest import TestCase


class Test(TestCase):
    def do_test(self, n, k, order, answer):
        submit = Q1700_SHC.sol(n, k, order)
        self.assertEqual(answer, submit)

    def test_1(self):
        self.do_test(2, 7, [2, 3, 2, 3, 1, 2, 7], 2)

    def test_2(self):
        self.do_test(3, 13, [2, 3, 4, 2, 3, 4, 1, 5, 5, 5, 2, 3, 2], 2)

    def test_3(self):
        self.do_test(2, 9, [1, 2, 3, 1, 2, 3, 1, 2, 3], 4)

    def test_4(self):
        self.do_test(3, 5, [1, 1, 1, 1, 2], 0)

    def test_5(self):
        self.do_test(3, 10, [1, 2, 3, 4, 4, 5, 2, 1, 1, 4], 3)

    def test_6(self):
        self.do_test(3, 5, [1, 1, 1, 1, 1], 0)

    def test_7(self):
        self.do_test(1, 10, [1, 2, 3, 4, 5, 6, 7, 1, 2, 3], 9)

    def test_8(self):
        self.do_test(4, 20, [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5], 4)
