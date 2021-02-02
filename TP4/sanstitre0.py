#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 13:50:05 2021

@author: thierry
"""
class Node:
     #constructeur (un arbre possede au minimum un noeud)
     def __init__(self, valeur, father=None):
         self.valeur = valeur
         self.enfant_gauche = None
         self.enfant_droit = None
         self.father = father
         print("Création du noeud", self.valeur,  "dans l'arbre enfant de", self.father, "\n")
     def insert_gauche(self, valeur):
         if self.enfant_gauche == None:
             self.enfant_gauche = Node(valeur, self.valeur)
         else:
             new_node = Node(valeur, self.enfant_gauche.valeur)
             new_node.enfant_gauche = self.enfant_gauche
             self.enfant_gauche = new_node
         return self.enfant_gauche
     def insert_droite(self, valeur):
         if self.enfant_droit == None:
             self.enfant_droit = Node(valeur, self.valeur)
             self.enfant_droit.father = self.valeur
         else:
             new_node = Node(valeur, self.enfant_droite.valeur)
             new_node.enfant_droit = self.enfant_droit
             self.enfant_droit = new_node
         return self.enfant_droit
     def get_valeur(self):
         """visualisation de la valeur du noeud"""
         return self.valeur
     def get_gauche(self):
         """Visualisation du sous arbre de gauche du noeud en cours"""
         return self.enfant_gauche
     def get_droit(self):
         """Visualisation du sous arbre de droite du noeud en cours"""
         return self.enfant_droit
     def get_father(self):
         """Visualisation du parent du noeud"""
         return self.father
     def is_leaf(self):
        return self.enfant_droit is None and self.enfant_gauche is None
     def noeud_complet(self):
         return self.enfant_droit != None and self.enfant_gauche != None
     def affiche(self): 
        if self.enfant_gauche != None and self.enfant_droit != None:
            return (self.valeur + "[" + self.enfant_droit.valeur + "," + self.enfant_gauche.valeur + "]")
        elif self.enfant_droit == None and self.enfant_gauche != None:
             return (self.valeur + "[" + self.enfant_gauche.valeur + "]")
        elif self.enfant_gauche == None and self.enfant_droit != None:
            return (self.valeur + "[" + self.enfant_droit.valeur + "]")
        else:
            return self.valeur
     def search(self, target_data):
         if self.valeur == target_data:
             return(self)
     
class Tree:
    def __init__(self, racine):
        self.racine = racine 
    def affiche(self):
        return (self.racine.get_valeur(), self.racine.get_gauche().affiche(), self.racine.get_droit().affiche())
    def search(self, target_data):
        return self.racine.search(target_data)
      
#création de la racine
racine = Node("A")
#En partant de la racine => création des enfants
B = racine.insert_gauche("B")
C = racine.insert_droite("C")
D = B.insert_gauche("D")
E = B.insert_droite("E")
F = C.insert_gauche("F")
G = C.insert_droite("G")
H = E.insert_gauche("H")
I = E.insert_droite("I")
J = D.insert_droite("J")

print(H.get_father())
print(racine.affiche())

tronc = Tree(racine)
print("Affichage arbre: ")
tronc.affiche()
#tronc.taille()
print("++++++++")
print(tronc.search("B"))