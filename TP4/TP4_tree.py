#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 14:47:37 2021

@author: thierry
"""
class TreeNode:
    def __init__(self, data:str):
        self.data = data
        self.link_left = None
        self.link_right = None
    def print_Tree(self):
        if self.link_right:
            self.link_right.print_Tree()
        print(self.data)
        if self.link_left:
            self.link_left.print_Tree()
    def is_leaf(self):
        return self.link_right is None and self.link_left is None
    def __str__(self):
        if self.is_leaf():     
            return str(self.data)
        else:
            return "[" + str(self.link_left) + ";" + str(self.link_right) + ";" + str(self.data) +"]"
    def __iter__(self):
        if self.link_left:
            for node in self.link_left:
                yield node
        yield self.data
        if self.link_right:
            for node in self.right:
                yield node
    #def find_node(self, node_target):empty_tree(self)
        #if node_target != self.data:
         
class Tree:
    def __init__(self, master_node):
        self.node_father = master_node
    def read_deep(self):
        print(self.node_father)
    def empty_tree(self):
        if not self.node_father:
            raise Exception("tree is empty")
    def added_node(self, add_node, target_node):
        new_node = TreeNode(add_node)
        if self.node_father == None
    def add_node(self, add_node, target_node):
        node = self.node_father
        add_node = TreeNode(add_node)
        while node.data != target_node:
            node = node.link_right
            
        while self.node_father is not None:
            if self.node_father.data == target_node:
                if self.node_father.link_right is None:
                    self.node_father.link_right = TreeNode(add_node)
                elif self.node_father.link_left is None:
                    self.node_father.link_left = TreeNode(add_node)
                else:
                    self.node_father = self.node_father.link_right
            else:
                self.node_father = self.node_father.link_right

tronc = TreeNode("tronc")
branche_1 = TreeNode("branch_1")
branche_2 = TreeNode("branch_2")
feuille_1 = TreeNode("feuille_1")
feuille_2 = TreeNode("feuille_2")
tronc.link_left = branche_1
tronc.link_right = branche_2
branche_1.link_left= feuille_1
branche_2.link_left = feuille_2
tronc.print_Tree()
tree = Tree(tronc)
tree.read_deep()

#print(n0)