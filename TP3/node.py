#!/usr/bin/env python3
# coding: utf-8
"""
Creating a class to define Node objects and give them attributes
"""
class Node:
    """
    Node Object
    ----------
    Parameters
    ----------
    param_data : int
        creation of the node with the param_data value
    param_link : None
        the param_link takes as value the memory path of the following node
    """
    def __init__(self, param_data, param_link=None):
        self.data = param_data
        self.link = param_link
    def __str__(self):
        """
        allows to display the list of nodes in a string format
        ----------
        Parameters
        ----------
        None
        ----------
        Returns
        ----------
        the list in string and a line break
        """
        liste = []
        node = self
        while node.link is not None:
            liste.append(node.data)
            node = node.link
        liste.append(node.data)
        return str(liste) + "\n"
    def equality(self, object_two):
        """
        check equality of two objects
        ----------
        Parameters
        ----------
        object_two : objet
            second object resembling the first
        ---------
        Returns
        -------
        Bool
            returns True if equality is confirmed otherwise False
        """
        return self.__dict__ == object_two.__dict__
