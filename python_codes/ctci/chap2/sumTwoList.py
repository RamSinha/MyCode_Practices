#!/usr/bin/python
from DoublyLinkedList import Node
from DoublyLinkedList import DoublyLinkedList


def sumTwoList(list1, list2, carry = 0):
    #base case
    # If both the lists are traversed and their no carryove value, it means no new node can be added.

    if list1 is None and list2 is None and carry is 0:
        return None

    value = carry

    if list1 is not None:
        value += list1.value

    if list2 is not None:
        value += list2.value

    temp = Node(value % 10)

    result = sumTwoList(list1 if list1 is None else list1.next, list2 if list2 is None else list2.next, value // 10)
    temp.next = result
    return temp


def sumTwoListFollowUp(list1, list2, carry = 0):
    stack1 = []
    stack2= []
    while list1:
        stack1.append(list1)
        list1= list1.next
    while list2:
        stack2.append(list2)
        list2= list2.next

    result = None
    last = None
    print (len(stack1) , len(stack2))
    while stack1 and stack2:
        top1 = stack1.pop()
        top2= stack2.pop()
        value = top1.value + top2.value + carry
        temp = Node(value % 10)
        if result is None:
            result = temp
            last = temp
        else:
            last.prev = temp
            temp.next = last
            last = temp
        carry = value // 10    
    leftOver = stack1 if not stack2 else stack2
    while leftOver:
        top = leftOver.pop()
        value = top.value + carry
        temp = Node(value % 10)
        last.prev = temp
        temp.next = last
        last = temp
        carry = value // 10
    if carry is not 0:
        value = carry
        temp = Node(value % 10)
        last.prev = temp
        temp.next = last
        last = temp
    return last


def printList(n):
    while n:
        print str(n.value) + '  --> ',
        n = n.next
    print (' None')    


def sameSize():
    n1 = Node(9)
    n2 = Node(1)
    n3 = Node(7)
    dll1 = DoublyLinkedList()
    dll1.insert(n1)
    dll1.insert(n2)
    dll1.insert(n3)
    dll1.printList()
    n1 = Node(2)
    n2 = Node(9)
    n3 = Node(5)
    dll2 = DoublyLinkedList()
    dll2.insert(n1)
    dll2.insert(n2)
    dll2.insert(n3)
    dll2.printList()
    n = sumTwoList(dll1.head, dll2.head)
    printList(n)

def differentSize():
    n1 = Node(9)
    n2 = Node(1)
    n3 = Node(7)
    n4 = Node(7)
    dll1 = DoublyLinkedList()
    dll1.insert(n4)
    dll1.insert(n1)
    dll1.insert(n2)
    dll1.insert(n3)
    dll1.printList()
    n1 = Node(2)
    n2 = Node(9)
    n3 = Node(5)
    dll2 = DoublyLinkedList()
    dll2.insert(n1)
    dll2.insert(n2)
    dll2.insert(n3)
    dll2.printList()
    n = sumTwoList(dll1.head, dll2.head)
    printList(n)

def sameSizeFollowUp():
    n1 = Node(9)
    n2 = Node(1)
    n3 = Node(7)
    dll1 = DoublyLinkedList()
    dll1.insert(n1)
    dll1.insert(n2)
    dll1.insert(n3)
    dll1.printList()
    n1 = Node(2)
    n2 = Node(9)
    n3 = Node(5)
    dll2 = DoublyLinkedList()
    dll2.insert(n1)
    dll2.insert(n2)
    dll2.insert(n3)
    dll2.printList()
    n = sumTwoListFollowUp(dll1.head, dll2.head)
    printList(n)

if __name__ == '__main__':
    #sameSize()
    #differentSize()
    sameSizeFollowUp()
