import unittest
from dlm import *

class TestDLM(unittest.TestCase):
    def test_initial_subterms(self):
        s1 = 'x'
        s2 = 'y'
        s3 = 'xz'
        t1 = 'zy'
        t2 = 'zz'

        terms = set([s1, s2, s3, t1, t2])
        self.assertEqual(initial_subterms(terms),
                         set(['', 'x', 'y', 'xz', 'z', 'zy', 'zz']))

if __name__ == '__main__':
    unittest.main()

