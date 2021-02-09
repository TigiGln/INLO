#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 10:43:02 2021
@author: thierry
Used to test the methods of the Linkedlist class
"""
#import sys
import unittest
import linkedList
#sys.path.append("..")
class TestLinkList(unittest.TestCase):
    """
    Test_linklist Object
    Parameters
    ----------
    None
    """
    def setUp(self):
        """
        method called for performing the tests, Creation
        of the test linked list
        """
        self.liste = linkedList.LinkedList(["g", "c", "f"])
    def test_list_empty(self):
        """
        Test allowing the verification of an empty list
        and the return Raise Exception
        """
        if str(self.liste) == "[]":
            with self.assertRaises(Exception, msg="List is empty"):
                self.liste.remove_node("x")
    def test_list_no_empty_add_value(self):
        """
        Test if a linked list is not empty after adding a node
        """
        #list_init = str(self.liste)
        self.liste.add_first(linkedList.Node("v"))
        #result= str(self.liste)
        self.assertFalse(self.liste.list_is_empty())
    def test_no_modif(self):
        """
        Test if the linked list is not modified when simultaneously adding
        and removing the same element
        """
        list_init = str(self.liste)
        self.liste.add_first(linkedList.Node("v"))
        self.liste.remove_node("v")
        result = str(self.liste)
        self.assertEqual(result, list_init)
    def test_first_element(self):
        """
        Test if the first element is the one added at the beginning
        of our linked list
        """
        self.liste.add_first(linkedList.Node("e"))
        result = str(self.liste)
        self.assertEqual(result[2], "e")
if __name__ == '__main__':
    unittest.main()
