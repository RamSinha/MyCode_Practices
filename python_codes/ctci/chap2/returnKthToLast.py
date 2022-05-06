#!/usr/bin/python
from DoublyLinkedList import Node
from DoublyLinkedList import DoublyLinkedList

def returnKth(head, k):
    steps = 0
    currentHead = head
    runner = head
    while runner.next and steps < k-1:
        currentHead = currentHead.next
        runner = runner.next
        steps += 1
    if steps < k -1:
        raise Exception('Not enough nodes in the list')
    runner = head
    while currentHead.next:
        currentHead = currentHead.next
        runner = runner.next
    return runner


def returnKthRecursive(head, k):
    if head is None:
        return 0
    myRankFromLast = returnKthRecursive(head.next, k) + 1
    if myRankFromLast == k :
        print head.value
    return myRankFromLast    

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
    kth = returnKth(dll.head, 1)
    print(kth.value)
    kth = returnKth(dll.head, 2)
    print(kth.value)
    returnKthRecursive(dll.head, 1)
    returnKthRecursive(dll.head, 2)
