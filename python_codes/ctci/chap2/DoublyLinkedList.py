#!/usr/bin/python

class Node:
    def __init__(self, value):
        self.next = None
        self.value = value
    
    def removeBindings(self):
        prevN = self.prev
        nextN = self.next

        if nextN is not None:
            nextN.prev = prevN
        if prevN is not None:
            prevN.next = nextN
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        pass

    def insert(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return

        node.next = self.head
        self.head.prev = node
        self.head = node
        return self.head

    def removeTail(self):
        if self.tail is None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return 

        self.tail = self.tail.prev
        self.tail.next = None
    
    def printList(self):
        head = self.head
        while head:
            print str(head.value) + ('' if head.next is None  else '--> '), 
            head = head.next
        print('')    

if __name__ == '__main__':
    n1 = Node(4)
    n2 = Node(-1)
    n3 = Node(6)
    n4 = Node(2)
    dll = DoublyLinkedList()
    dll.insert(n1)
    dll.insert(n2)
    dll.insert(n3)
    dll.insert(n4)
    dll.printList()


