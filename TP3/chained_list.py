#!/usr/bin/env python3
# coding: utf-8
"""
This class will make it possible to take a list of values ​​to create nodes for each.
It will allow you to act on the chained list by adding or removing nodes
"""
from node import Node

class Chainedlist:
    """
    Chained list Object
    Parameters
    ----------
    list_elt : list()
        list that we want to transfert in a chained list of Node object
    """
    def __init__(self, list_elt):
        self.first_node = None
        if list_elt != None and len(list_elt) != 0:
            node_link = None
            for index in range((len(list_elt)-1), -1, -1):
                node = list_elt[index]
                node_link = Node(node, node_link)
            self.first_node = node_link
    def get(self, index):
        if self.first_node == None:
            raise ValueError("Node empty")
            
    def recursion(self, index, node):
        print(index, node)
        if node is not None:
            return index, node
        elif index == 0:
            return index, node
        else:
            return self.recursion(index-1, node.link)
        
    def __str__(self):
        """
        Allows to display the list of nodes in a string format
        ----------
        Parameters
        ----------
        None
        ----------
        Returns
        ----------
        the list in string
        """
        return str(self.first_node)
    def insert_node_after(self, before_element, new_element):
        """
        Insert a new node after the node with the value == before_element
        ----------
        Parameters
        ----------
        before_element : int
            Search for the node preceding the addition
        new_element : int
            Item to add to the linked list
        ---------
        Returns
        ---------
        None
            Insert a new node after a defined node
        """
        element = self.first_node
        new_element = Node(new_element)
        while element.data != before_element:
            element = element.link
        new_element.link = element.link
        element.link = new_element
    def delete_node(self, element_del):
        """
        Delete all node(s) data == element_del
        ----------
        Parameters
        ----------
        element_del : int
            searched element to delete thanks to his value
        ----------
        Returns
        ----------
        print a string
            Delete the chosen node
        """
        element = self.first_node
        if element.data != element_del:
            while element.link.data != element_del:
                element = element.link
            element.link = element.link.link
        else:
            element.data = element.link.data
            element.link =  element.link.link
        print("deletion display")
        