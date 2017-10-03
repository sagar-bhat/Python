'''
Stack Implementation

'''


class Stack(object):
    ''' Represents a Stack Data Structure '''

    def __init__(self):
        self._stack = []

    def push(self, data):
        ''' Pushes data into the Stack '''
        self._stack.append(data)

    def pop(self):
        ''' Returns and pops the top element from the stack '''
        return self._stack.pop()

    @property
    def get_stack(self):
        ''' Returns the Entire Stack '''
        return self._stack

    @property
    def top(self):
        ''' Returns the top element from the stack '''
        return self._stack[-1]

if __name__ == '__main__':

    stack = Stack()
    dataList = [10, 20, 30, 40, 50]

    for data in dataList:
        stack.push(data)

    print"Popped Element:", stack.pop()
    print"Popped Element:", stack.pop()
    print"Top Element:", stack.top

