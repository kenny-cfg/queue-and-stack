import unittest
from queue import Queue


class TestQueue(unittest.TestCase):
    def test_can_initialize(self):
        queue = Queue()


if __name__ == '__main__':
    unittest.main()
