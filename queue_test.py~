'''
Test Cases for Validating the Functionalities
of implemented Queue Data Structure

'''

import unittest
from queue import Queue


class QueueTest(unittest.TestCase):

    def setUp(self):
        '''
        Creates an Object of Queue
        for each Test case

        '''

        self.queue = Queue()
        data = [1, 2, 3, 4]
        for x in data:
            self.queue.enqueue(x)

    def test_enqueue(self):
        '''
        Tests whether the objects in a queue
        are inserted properly

        '''

        self.queue.enqueue(5)
        self.assertEqual(self.queue.getRear, 5)
        self.queue.enqueue(6)
        self.assertEqual(self.queue.getRear, 6)

    def test_dequeue(self):
        '''
        Tests whether the objects in a queue
        are dequeued properly

        '''

        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)

    def test_getFront_property(self):
        '''
        Tests whether the Front points to the
        correct Element in the Queue

        '''

        self.assertEqual(self.queue.getFront, 1)
        self.queue.dequeue()
        self.assertEqual(self.queue.getFront, 2)

    def test_getRear_property(self):
        '''
        Tests whether the Rear points to the
        correct Element in the Queue

        '''

        self.assertEqual(self.queue.getRear, 4)
        self.queue.enqueue(5)
        self.assertEqual(self.queue.getRear, 5)

    def tearDown(self):
        '''
        Deletes the created queue object
        after each Test case

        '''

        del self.queue


if __name__ == '__main__':

    unittest.main()

