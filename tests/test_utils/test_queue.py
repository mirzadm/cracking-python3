"""Unit tests for queue.py."""

import unittest

from src.utils.queue import Queue


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue_obj = Queue()

    def test_init(self):
        self.assertIsNone(self.queue_obj.head)
        self.assertIsNone(self.queue_obj.tail)
        self.assertEqual(self.queue_obj.size(), 0)
        self.assertTrue(self.queue_obj.is_empty())

    def test_enq_deq_one_element(self):
        data = 5
        self.queue_obj.enqueue(data)
        self.assertEqual(self.queue_obj.size(), 1)
        data_copy = self.queue_obj.dequeue()
        self.assertEqual(data_copy, data)
        self.assertEqual(self.queue_obj.size(), 0)
        self.assertTrue(self.queue_obj.is_empty())

    def test_enq_deq_two_elements(self):
        data_list = [5, 6]
        for data in data_list:
            self.queue_obj.enqueue(data)
        self.assertEqual(self.queue_obj.size(), 2)
        for data in data_list:
            data_copy = self.queue_obj.dequeue()
            self.assertEqual(data_copy, data)
        self.assertEqual(self.queue_obj.size(), 0)
        self.assertTrue(self.queue_obj.is_empty())

    def test_deq_on_empty_queue(self):
        self.assertRaises(KeyError, self.queue_obj.dequeue)     


if __name__ == '__main__':
    unittest.main()