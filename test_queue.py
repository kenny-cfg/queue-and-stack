import unittest
from queue import Queue


class TestQueue(unittest.TestCase):
    def test_can_initialize(self):
        queue = Queue()
        self.assertIsNotNone(queue)

    def test_popping_is_fifo(self):
        queue = Queue()
        queue.push(1)
        queue.push(2)
        queue.push(3)

        self.assertEqual(queue.pop(), 1)
        self.assertEqual(queue.pop(), 2)
        self.assertEqual(queue.pop(), 3)


if __name__ == '__main__':
    unittest.main()
