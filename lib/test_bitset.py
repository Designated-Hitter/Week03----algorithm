from unittest import TestCase
from lib.bitset import Bitset


class Test(TestCase):
    def test_all_any(self):
        for n in range(1, 10000):
            b = Bitset(n)
            self.assertFalse(b.any())
            self.assertFalse(b.all())
            b.set(0)
            self.assertTrue(b.any())
            for i in range(n):
                b.set(i)
            self.assertTrue(b.all())
