'''
Queue Implementation

'''


class Queue(object):
    '''
    Represents Queue Data Structure

    '''

    def __init__(self):
        self._queue = []

    def enqueue(self, data):
        '''
        Inserts a data element in
        the queue from Rear End

        '''

        self._queue.append(data)

    def dequeue(self):
        '''
        Returns and removes the Front
        element from the queue

        '''

        return self._queue.pop(0)

    @property
    def getRear(self):
        '''
        Returns the most recently added
        element in the queue, pointed by Rear

        '''

        return self._queue[-1]

    @property
    def getFront(self):
        '''
        Returns the least recently added
        element in the queue, pointed by Front

        '''

        return self._queue[0]

    @property
    def getQueue(self):
        '''
        Returns the entire Queue

        '''

        return self._queue


if __name__ == '__main__':

    que = Queue()
    dataList = [1, 2, 3, 4]

    for data in dataList:
        que.enqueue(data)

    print "Front Element:{0}".format(que.getFront)
    print "Rear Element: {0}".format(que.getRear)
    print "Dequeued Element: {0}".format(que.dequeue())
    print "Front Element:{0}".format(que.getFront)

