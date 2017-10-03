'''
Test cases for validating
operations on a Binary Tree

'''

import unittest
from binary_tree import BinaryTree


class BinaryTree_test(unittest.TestCase):

    def setUp(self):
        '''
        Creates an instance of BinaryTree
        to be used by each Test case

        '''

        self.binarytree = BinaryTree()
        elements = [20, 15, 17, 24, 22, 18, 23]

        for x in elements:
            self.binarytree.insert(x)

    def test_insert(self):
        '''
        Checks whether elements are inserted
        properly at correct positions or not

        '''

        tree = BinaryTree()
        self.assertEqual(tree.insert(33), "Root Inserted")
        self.assertEqual(tree.insert(14), "Node Inserted")
        self.assertEqual(tree.insert(35), "Node Inserted")
        self.assertEqual(tree.insert(34), "Node Inserted")

    def test_level_order(self):
        '''
        Checks whether the binary tree elements are properly
        printed in Level Order i.e. Breadth First Format

        '''

        self.assertEqual(
                        self.binarytree.levelOrder(),
                        [20, 15, 24, 17, 22, 18, 23]
                        )

    def test_preorder(self):
        '''
        Checks whether the binary tree elements are
        properly printed in PreOrder Format or not.

        '''

        self.assertEqual(
                        self.binarytree.preOrder(),
                        [20, 15, 17, 18, 24, 22, 23]
                        )

    def test_inorder(self):
        '''
        Checks whether the binary tree elements are
        properly printed in InOrder Format or not.

        '''

        self.assertEqual(
                        self.binarytree.inOrder(),
                        [15, 17, 18, 20, 22, 23, 24]
                        )

    def test_postorder(self):
        '''
        Checks whether the binary tree elements are
        properly printed in PostOrder Format or not.

        '''

        self.assertEqual(
                        self.binarytree.postOrder(),
                        [18, 17, 15, 23, 22, 24, 20]
                        )

    def test_search(self):
        '''
        Check whether the entered element exists
        in the Binary Tree or not

        '''

        self.assertEqual(self.binarytree.search(15), "Value Exists")
        self.assertEqual(self.binarytree.search(13), "Value Doesn't Exist")

    def tearDown(self):
        '''
        Deletes the BinaryTree Instance
        after each Test case

        '''

        del self.binarytree


if __name__ == '__main__':

    unittest.main()

