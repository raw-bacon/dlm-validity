import unittest
from dlm import *
from z3 import Int, Implies

s1 = 'x'
s2 = 'y'
s3 = 'xz'
t1 = 'zy'
t2 = 'zz'

terms = set([s1, s2, s3, t1, t2])

class TestDLM(unittest.TestCase):
    def test_initial_subterms(self):
        self.assertEqual(initial_subterms(terms),
                         set(['', 'x', 'y', 'xz', 'z', 'zy', 'zz']))

    def test_sigma(self):
        expected = set()
        # x: nothing
        # y: {uy = s2, vy = t1}, {uy = t1, vy = s2}
        expected.add(Implies(
            Int('') <= Int('z'),
            Int('y') <= Int('zy')
        ))
        expected.add(Implies(
            Int('z') <= Int(''),
            Int('zy') <= Int('y')
        ))
        # z: {uz = s3, vz = t2}, {uz = t2, vz = s3}
        expected.add(Implies(
            Int('x') <= Int('z'),
            Int('xz') <= Int('zz')
        ))
        expected.add(Implies(
            Int('z') <= Int('x'),
            Int('zz') <= Int('xz')
        ))
        self.assertEqual(sigma(terms), expected)

if __name__ == '__main__':
    unittest.main()

