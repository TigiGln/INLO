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
        self.liste1 = linkedList.LinkedList()
        self.liste2 = linkedList.LinkedList(["g", "c", "f"])
    def test_list_empty(self):
        """
        Test if the list is empty
        """
        self.assertTrue(str(self.liste1.list_is_empty()))
    def test_no_delete_list_empty(self):
        """
        Test allowing the verification of an empty list
        and the return Raise Exception
        """
        with self.assertRaises(Exception, msg="List is empty"):
            self.liste1.remove_node("x")
        print("No element can be deleted in this list since it is empty")
    def test_list_no_empty_add_value(self):
        """
        Test if a linked list is not empty after adding a node
        """
        self.liste1.add_first(linkedList.Node("v"))
        self.assertFalse(self.liste1.list_is_empty())
    def test_no_modif(self):
        """
        Test if the linked list is not modified when simultaneously adding
        and removing the same element
        """
        list_init = str(self.liste2)
        self.liste2.add_first(linkedList.Node("v"))
        self.liste2.remove_node("v")
        result = str(self.liste2)
        self.assertEqual(result, list_init)
    def test_first_element(self):
        """
        Test if the first element is the one added at the beginning
        of our linked list
        """
        self.liste2.add_first(linkedList.Node("e"))
        result = list(self.liste2)
        self.assertEqual(str(result[0]), "e")
if __name__ == '__main__':
    unittest.main()
