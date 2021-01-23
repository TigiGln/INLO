# coding: utf-8

from node import Node
from chainedList import ChainedList

def test_print_node():
    n1 = Node(1)
    n2 = Node(5)
    n1.link = n2
    print(n1)

if __name__ == "__main__":
    # just a test to see how the __str__ method of node work's
    test_print_node()
    chained_list = ChainedList([1,5,6,12,34])