import heapq

class Node(object):
    def __init__(self, num):
        self.num = num
    def __lt__(self, other):
        return self.num > other.num
    def __str__(self):
        return str(self.num)
    def __repr__(self):
        return self.__str__()

def heapify(seq):
    l = map(lambda x: Node(x), seq)
    heapq.heapify(l)
    return map(lambda x : x.num, l)

if __name__ == '__main__':
    print heapify(map(lambda x : int(x), raw_input("enter comma seperated ints \n").split(",")))
