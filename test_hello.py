import math
import unittest
import hello
import pytest
import numpy as np

class TestHello(unittest.TestCase):
    def test_hello(self):        
        self.assertEqual(hello.hello(), "Hello, world!")

    def test_add(self):
        self.assertEqual(hello.add(1, 2), 3)
        self.assertEqual(hello.add(1, 2.34), 3.34)
        self.assertEqual(hello.add(-4, 2), -2)

    def test_sub(self):
        self.assertEqual(hello.sub(2, 2), 0)
        self.assertEqual(hello.sub(2, -2), 4)
        self.assertAlmostEqual(hello.sub(-2.2, -2), -0.2, places=7, msg=None, delta=None)

    def test_mul(self):
        self.assertEqual(hello.mul(2, 2.1), 4.2)
        self.assertEqual(hello.mul(-3, 4), -12)
        self.assertEqual(hello.mul(2, 0), 0)

    def test_div(self):
        self.assertAlmostEqual(hello.div(-2, 3), -0.66666666, places=7, msg=None, delta=None)
        self.assertEqual(hello.div(5, 2), 2.5)
        with pytest.raises(ZeroDivisionError, match="division by zero"): 
            1 / 0

    def test_sqrt(self):
        self.assertAlmostEqual(hello.sqrt(4.1), 2.02484567313, places=7, msg=None, delta=None)
        self.assertAlmostEqual(hello.sqrt(2), 1.41421356237, places=7, msg=None, delta=None)
        self.assertEqual(hello.sqrt(0), 0)
        self.assertTrue(hello.sqrt(-2), math.isnan(np.sqrt(-2)))
    
    def test_power(self):
        self.assertEqual(hello.power(4, 2), 16)
        self.assertAlmostEqual(hello.power(2, -3.4), 0.0947322854, places=7, msg=None, delta=None)
        self.assertEqual(hello.power(0, 0), 1)

    def test_log(self):
        self.assertEqual(hello.log(1), 0)
        self.assertEqual(hello.log(np.e), 1)
        self.assertTrue(hello.log(-4.5), math.isnan(np.log(-4.5)))

    def test_exp(self):
        self.assertEqual(hello.exp(0), 1)
        self.assertAlmostEqual(hello.exp(1), 2.718281828459045, places=7, msg=None, delta=None)
        self.assertAlmostEqual(hello.exp(-0.5), 0.60653065971, places=7, msg=None, delta=None)

    def test_cos(self):
        self.assertEqual(hello.cos(0), 1)
        self.assertAlmostEqual(hello.cos(1), 0.5403023058681398, places=7, msg=None, delta=None)
        self.assertAlmostEqual(hello.cos(0.5), 0.8775825618903728, places=7, msg=None, delta=None)
        self.assertAlmostEqual(hello.cos(-0.5), 0.8775825618903728, places=7, msg=None, delta=None)

    def test_tan(self):
        self.assertEqual(hello.tan(0), 0)
        self.assertAlmostEqual(hello.tan(1), 1.5574077246549023, places=7, msg=None, delta=None)
        self.assertAlmostEqual(hello.tan(0.5), 0.5463024898437905, places=7, msg=None, delta=None)
        self.assertAlmostEqual(hello.tan(-0.5), -0.5463024898437905, places=7, msg=None, delta=None)

    def test_cot(self):
        self.assertEqual(hello.cot(0), float("inf"))
        self.assertAlmostEqual(hello.cot(1), 0.6420926159343306, places=7, msg=None, delta=None)
        self.assertAlmostEqual(hello.cot(0.5), 1.830487721712452, places=7, msg=None, delta=None)
        self.assertAlmostEqual(hello.cot(-0.5), -1.830487721712452, places=7, msg=None, delta=None)


if __name__ == "__main__":
    unittest.main()
