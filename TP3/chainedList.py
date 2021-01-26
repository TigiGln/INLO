#!/usr/bin/env python3
# coding: utf-8
from node import Node

class ChainedList(Node):
    """
    Chained list Object
    Parameters
    ----------
    nodes : list
        list that we want to transfert in a chained list of Node object
    """
    def __init__(self, nodes):
        self.first_node = nodes[0] #list empty
        self.node = list(nodes)
        
    def __str__(self):
        liste = []
        for elt in self.node:
            liste.append(elt)
        return str(liste)
    
    def empty_list(self):
        if self.first_node is None:
            print("This list is empty")
        else:
            print("this list isn't empty")
    
    def list_size(self):
        element = self.first_node
        length = 0
        while element is not None:
            length += 1
            element = element.link
            return length
        
    def add_start(self, first_element):
        first_element.link = self.first_node
        self.first_node = first_element
        self.node.append(first_element)
        print(self.node)
   
    def add_end(self, end_element):
        element = self.first_node
        while element.link is not None:
            element = element.link
        element.link = end_element
    
    def insert_node_after(self, before_element, new_element):
        """
        insert a new node after the node with the value == before_element
        Parameters
        ----------
        before_element : searched data
        new_element : node to insert
        """
        new_element.link = before_element.link
        before_element.link = new_element
        return self
      
    def delete_node(self, element, before_element):
        """
        delete all node(s) value == data
        Parameters
        ----------
        data : searched data to delete
        """
        if element == self.first_node:
            self.first_node = element.link
        elif element == before_element.link:
            before_element.link = element.link
            
