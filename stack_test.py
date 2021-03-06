'''
Unit Testing for Stack Implementation

'''

import unittest
from stack import Stack


class StackTest(unittest.TestCase):

    def setUp(self):
        ''' Creates a Stack Object '''
        self.stk = Stack()
        data = [1, 2, 3, 4, 5]
        for x in data:
            self.stk.push(x)

    def test_push(self):
        ''' To check whether object is pushed on Stack or not '''
        self.stk.push(6)
        self.assertEqual(self.stk.top, 6)

    def test_pop(self):
        ''' To check whether objects are popped correctly or not '''
        self.assertEqual(self.stk.pop(), 5)
        self.assertEqual(self.stk.pop(), 4)

    def test_top_property(self):
        ''' To check whether the top of the Stack is returned correctly'''
        self.assertEqual(self.stk.top, 5)
        self.stk.pop()
        self.assertEqual(self.stk.top, 4)

    def tearDown(self):
        ''' Deletes the created Stack '''
        del self.stk

if __name__ == '__main__':

    unittest.main()

