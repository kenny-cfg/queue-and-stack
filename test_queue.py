import unittest
from queue import Queue


class TestQueue(unittest.TestCase):
    def test_can_initialize(self):
        queue = Queue()
        self.assertIsNotNone(queue)

    def test_popping_is_fifo(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)

    def test_can_instantiate_with_initial_values(self):
        queue = Queue(1, 2, 3)

        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)


if __name__ == '__main__':
    unittest.main()
