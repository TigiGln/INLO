#!/usr/bin/env python3
# coding: utf-8
"""
Allows to launch and test our Node and Chainedlist classes
"""
from node import Node
from chained_list import Chainedlist
def test_print_node():
    """
    Test the display of nodes
    ----------
    Parameters
    ----------
    None
    ----------
    Returns
    ----------
    print a string
        display the first node
    """
    node1 = Node(1)
    node2 = Node(5)
    node1.link = node2
    print(node1)
if __name__ == "__main__":
    test_print_node()
    # just a test to see how the __str__ method of node work's
    # chained_list = Chainedlist([1,5,6,12,34])
    # print(chained_list)
    # chained_list.insert_node_after(6, 9)
    # chained_list.insert_node_after(1, 3)
    # print("insert display")
    # print(chained_list)
    # chained_list.delete_node(9)
    # print(chained_list)
    # chained_list.delete_node(1)
    # print(chained_list)
    # l = Chainedlist([])
    # l.get(None)
    llist = Chainedlist(["a", "b", "c", "d", "e"])
    llist.recursion(3, llist.first_node)