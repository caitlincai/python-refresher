import unittest
import hello

class TestHello(unittest.TestCase):
    def test_hello(self):        
        self.assertEqual(hello.hello(), "Hello, world!")
        self.assertEqual(hello.hello() + " How are you?", "Hello, world! How are you?")
        self.assertEqual(hello.hello() + " I'm Caitlin!", "Hello, world! I'm Caitlin!")

    def test_sin(self):
        self.assertEqual(hello.sin(0), 0)
        self.assertEqual(hello.sin(1), 0.8414709848078965)
        self.assertEqual(hello.sin(0.5), 0.479425538604203)

    def test_cos(self):
        self.assertEqual(hello.cos(0), 1)
        self.assertEqual(hello.cos(1), 0.5403023058681398)
        self.assertEqual(hello.cos(0.5), 0.8775825618903728)

    def test_tan(self):
        self.assertEqual(hello.tan(0), 0)
        self.assertEqual(hello.tan(1), 1.557407724654902)
        self.assertEqual(hello.tan(0.5), 0.5463024898437905)

    def test_cot(self):
        self.assertEqual(hello.cot(0), float("inf"))
        self.assertEqual(hello.cot(1), 0.6420926159343308)
        self.assertEqual(hello.cot(0.5), 1.830487721712452)


if __name__ == "__main__":
    unittest.main()
