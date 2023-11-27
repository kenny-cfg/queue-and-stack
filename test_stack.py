import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    def test_can_initialize(self):
        stack = Stack()
        self.assertIsNotNone(stack)

    def test_popping_is_fifo(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)

    def test_can_instantiate_with_initial_values(self):
        stack = Stack(1, 2, 3)

        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)


if __name__ == '__main__':
    unittest.main()
