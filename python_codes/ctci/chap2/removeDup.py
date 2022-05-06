#!/usr/bin/python
from DoublyLinkedList import Node
from DoublyLinkedList import DoublyLinkedList

def removeDups(linkedList):
    cache = {}
    if linkedList is None:
        return linkedList
    head = linkedList
    prev = None
    while head:
        if head.value in cache:
            if head.next is not None:
                head.next.prev = prev
            prev.next = head.next
            head.prev = None
            head = head.next
            continue
        cache[head.value] = True    
        prev = head
        head = head.next

def removeDupsWithOutSpace(head):
    currentNode = head
    while currentNode:
        prev = currentNode
        nextNode = currentNode.next
        while nextNode:
            if nextNode.value == currentNode.value:
                if nextNode.next is not None:
                    nextNode.next.prev = prev
                prev.next = nextNode.next
                nextNode = nextNode.next
                continue
            prev = nextNode
            nextNode = nextNode.next
        currentNode = currentNode.next




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
    removeDupsWithOutSpace(dll.head)
    print ('--after cleanup--')
    dll.printList()
