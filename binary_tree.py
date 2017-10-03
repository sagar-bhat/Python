'''
Binary Tree Implementation

'''

from stack import Stack
from queue import Queue


class BinaryTree(object):
    '''
    Represents a Binary Tree

    '''

    def __init__(self):
        '''
        Constructor for Binary Tree

        '''

        self.root = None

    class Node(object):
        '''
        Represents a Node of a Binary Tree

        '''

        def __init__(self, value=None):
            '''
            Constructor for Node

            '''

            self.left = None
            self.value = value
            self.right = None

        def __repr__(self):

            return "{0}".format(self.value)

    def insert(self, value):
        '''
        Inserts a Node in the Binary Tree

        '''

        if self.root is None:
            # Check if the node is root Node
            self.root = self.Node(value)
            return "Root Inserted"
        else:
            current = self.root
            while True:
                # Insert Node on the left of current node
                if value < current.value:
                    if not current.left:
                        current.left = self.Node(value)
                        return "Node Inserted"
                    else:
                        current = current.left
                # Insert Node on the right of current node
                elif value > current.value:
                    if not current.right:
                        current.right = self.Node(value)
                        return "Node Inserted"
                    else:
                        current = current.right
                # If a Duplicate Node already exists
                elif value == current.value:
                    return "Duplicate Entry"

    def levelOrder(self):
        '''
        Prints the nodes of Binary
        Tree in Breadth-First Format

        '''

        que = Queue()
        # Store the output in another queue
        traversalQue = Queue()

        if self.root is None:
            return que
        temp = self.root
        que.enqueue(self.root)

        while que.getQueue:
            temp = que.dequeue()
            traversalQue.enqueue(temp.value)

            # Enqueue left and right children of dequed node
            if temp.left:
                que.enqueue(temp.left)
            if temp.right:
                que.enqueue(temp.right)

        return traversalQue.getQueue

    def preOrder(self):
        '''
        Prints the nodes of Binary
        Tree in Pre-Order Format Iteratively

        '''

        stk = Stack()
        que = Queue()

        if self.root is None:
            return que.getQueue
        stk.push(self.root)

        while stk.get_stack:
            current = stk.pop()
            que.enqueue(current.value)

            if current.right:
                stk.push(current.right)
            if current.left:
                stk.push(current.left)

        return que.getQueue

    def postOrder(self):
        '''
        Prints the nodes of Binary
        Tree in Post-Order Format Iteratively

        '''

        stk1 = Stack()
        stk2 = Stack()
        que = Queue()

        if self.root is None:
            return que.getQueue

        stk1.push(self.root)
        # While Stack is not empty
        while stk1.get_stack:
            node = stk1.pop()
            stk2.push(node)

            if node.left:
                stk1.push(node.left)
            if node.right:
                stk1.push(node.right)

        while stk2.get_stack:
            que.enqueue(stk2.pop().value)

        return que.getQueue

    def inOrder(self):
        '''
        Prints the nodes of Binary
        Tree in In-Order Format Iteratively

        '''

        stk = Stack()
        que = Queue()
        done = 0

        if self.root is None:
            return que.getQueue
        else:
            current = self.root

        while not done:
            if current:
                stk.push(current)
                current = current.left
            else:
                if stk.get_stack:
                    current = stk.pop()
                    que.enqueue(current.value)
                    current = current.right
                else:
                    done = 1

        return que.getQueue

    def search(self, value):
        '''
        Searches the provided value in
        the Binary Tree. Returns whether
        the value exists in the tree or not.

        '''

        current = self.root

        while current is not None:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            elif value == current.value:
                return "Value Exists"
        return "Value Doesn't Exist"


if __name__ == '__main__':

    tree = BinaryTree()
    dataList = [30, 20, 10, 40, 25, 50, 35, 37]

    for data in dataList:
        tree.insert(data)

    print "\nLevel Order Traversal:"
    print tree.levelOrder()

    print "\nPreOrder Traversal:"
    print tree.preOrder()

    print "\nInOrder Traversal:"
    print tree.inOrder()

    print "\nPostOrder Traversal:"
    print tree.postOrder()

    print "\nChecking if '40' exists in BinaryTree:"
    print tree.search(40)
    print "\nChecking if '16' exists in BinaryTree:"
    print tree.search(16)

