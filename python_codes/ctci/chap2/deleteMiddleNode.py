#!/usr/bin/python
from DoublyLinkedList import Node
from DoublyLinkedList import DoublyLinkedList

def deleteMiddleNode(head):
    head.removeBindings()

if __name__ == '__main__':
    n1 = Node(4)
    n2 = Node(-1)
    n3 = Node(6)
    n4 = Node(2)
    n5 = Node(2)
    dll = DoublyLinkedList()
    dll.insert(n1)
    dll.insert(n2)
    dll.insert(n3)
    dll.insert(n4)
    dll.insert(n5)
    dll.printList()
    deleteMiddleNode(n3)
    dll.printList()

