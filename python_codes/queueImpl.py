#!/usr/bin/python
class Queue(object):
    def __init__(self):
        self.capacity = 5
        self.front = 0
        self.end = 0
        self.q = [None for _ in range(self.capacity)]

    def isEmpty(self):
        return self.front == self.end


    def isFull(self):
        return (self.end + 1) % self.capacity == self.front


    def insert(self, e):
        if self.isFull():
            raise Exception('Queue is full')
        self.q[self.end] = e
        self.end = (self.end + 1 ) % self.capacity
        
    def remove(self):
        if self.isEmpty():
            raise Exception ('Queue is empty')
        item = self.q[self.front]
        self.front = ( self.front + 1 ) % self.capacity
        return item


if __name__ == '__main__':
    q= Queue()
    q.insert(1)
    q.insert(2)
    q.insert(3)
    q.insert(4)
    while not q.isEmpty():
        print (q.remove())
    q.insert(1)
    q.insert(2)
    q.insert(3)
    q.insert(4)
    while not q.isEmpty():
        print (q.remove())


