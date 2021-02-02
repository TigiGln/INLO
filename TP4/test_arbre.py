#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 13:24:56 2021

@author: thierry
"""
class Noeud:
     #constructeur (un arbre possede au minimum un noeud)
     def __init__(self, valeur):
         self.valeur = valeur
         self.enfant_gauche = None
         self.enfant_droit = None
         print("Création du noeud", self.valeur,  "dans l'arbre", "\n")
     def insert_gauche(self, valeur):
         if self.enfant_gauche == None:
             self.enfant_gauche = Noeud(valeur)
         else:
             new_node = Noeud(valeur)
             new_node.enfant_gauche = self.enfant_gauche
             self.enfant_gauche = new_node
         return self.enfant_gauche
     def insert_droit(self, valeur):
         if self.enfant_droit == None:
             self.enfant_droit = Noeud(valeur)
         else:
             new_node = Noeud(valeur)
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
     def is_leaf(self):
        return self.enfant_droit is None and self.enfant_gauche is None
    
    
    
     def affiche(self):
         string = ""
         if self.valeur != None:
             string += self.valeur
         
         if self.get_gauche() != None:
             string += "(" + self.get_gauche().affiche()
         else:
             string += "(None;"
         if self.get_droit() != None:
             string += ";" + self.get_droit().affiche() + ")"
         else:
             string += ";None)"
         return string
             
             
#afficher l'arbre sous forme d'un tuple
#def affiche(T):
#   if T != None:
#       return (T.get_valeur(), affiche(T.get_gauche()), affiche(T.get_droit()))
def affiche_niveau(T, niveau:int):
    """Affiche le niveau d'un arbre"""
    if T != None:
        if niveau == 1:
            print(" -", T.valeur, end="")#Affiche la valeur du noeud
        else:
            affiche_niveau(T.get_gauche(), niveau-1)#affiche le niveau inférieur gauche
            affiche_niveau(T.get_droit(), niveau-1)#affiche le niveau inférieur droit
def hauteur(T):
    """Calcul de la hauteur d'un arbre"""
    if T == None:
        return 0 #cas où l'arbre est vide
    else:
        return 1 + max(hauteur(T.get_gauche()), hauteur(T.get_droit()))
def taille(T):
    """Calcul de la taille de l'arbre"""
    if T == None:
        return 0 #cas où l'arbre est vide
    else:
        return 1 + taille(T.get_gauche()) + taille(T.get_droit())
#parcours profondeur 1
def parcours_infixe(T):
    """Affichage du parcours infixe d'un arbre (lecture gauche racine droite)"""
    if T != None:
        parcours_infixe(T.get_gauche())#sous arbre de gauche
        print(' -', T.valeur, end="")#Affiche la valeur du Noeud
        parcours_infixe(T.get_droit())#sous arbre de droite
#parcours profondeur 2
def parcours_suffixe(T):
    """Affichage du parcours suffixe d'un arbre (lecture gauche droite racine"""
    if T != None:
        parcours_suffixe(T.get_gauche())#sous arbre de gauche
        parcours_suffixe(T.get_droit())#sous arbre de droite
        print(' -', T.valeur, end ='') #Affiche la valeur du Noeud
#parcours profondeur 3
def parcours_prefixe(T):
    """Affichage du parcours préfixe d'un arbre (lecture racine gauche droite) """
    if T != None:
        print(' -', T.valeur,end="")#Affiche la valeur du noeud
        parcours_prefixe(T.get_gauche())#parcours sous arbre de gauche
        parcours_prefixe(T.get_droit())#parcours sous arbre de droite
#parcours largeur 1
def parcours_largeur_1(T):
    """Affichage du parcours en largeur d'un arbre """
    if T != None:
        #on initialise la file avec l'arbre complet
        file = []
        file.append(T)
        while len(file) > 0:
            #on affiche puis on retire le premier élément
            print(" -", file[0].valeur, end="")
            noeud = file.pop(0) #On le supprime de la file et on récupère sa valeur
            #Ajout de l'enfant de gauche de l'élément retiré
            if noeud.get_gauche() != None:
                file.append(noeud.get_gauche())
            #Ajout de l'enfant de droite de l'élement retiré
            if noeud.get_droit() != None:
                file.append(noeud.get_droit())
#parcours largeur 2
def parcours_largeur_2(T):
    """Affiche le parcours de l'arbre en largeur """
    h = hauteur(T)#Calcul de la hauteur de l'arbre total
    for niveau in range(1, h+1, 1):
        affiche_niveau(T, niveau)#affichage pour chaque niveau 1, le niveau entre 1 et h
        
def insertion_par_target(T, target):
    """Parcours l'arbre et trouve le target"""
    if T != None:
        liste = []
        liste.append(T)
        while len(liste) > 0:
            noeud =  liste.pop(0)
            if noeud.get_gauche() != None:
                print(noeud.get_gauche().valeur)
                liste.append(noeud.get_gauche())
            if noeud.get_droit() != None:
                print(noeud.get_gauche().valeur)
    
    
            
            
            
#création de la racine
racine = Noeud("A")
#En partant de la racine => création des enfants
B = racine.insert_gauche("B")
C = racine.insert_droit("C")
D = B.insert_gauche("D")
E = B.insert_droit("E")
F = C.insert_gauche("F")
G = C.insert_droit("G")
H = E.insert_gauche("H")

#Affiche l'arbre en entier à partir de la racine
print("Affichage arbre: ")
print(racine.affiche(), "\n")
print("Affichage niveau: ")
affiche_niveau(racine, 2)
print("\nAffichage hauteur:")
print("Hauteur = ", hauteur(racine))
print("Affichage taille: ")
print("Taille = " , taille(racine))
print("\n" + "Affichage parcours profondeur 1 : ")
parcours_infixe(racine)
print("\n" + "Affichage parcours profondeur 2 : ")
parcours_suffixe(racine)
print("\n" + "Affichage parcours profondeur 3 : ")
parcours_prefixe(racine)
print("\n" + "Affichage parcours largeur 1 : ")
parcours_largeur_1(racine)
print("\n" + "Affichage parcours largeur 2 :")
parcours_largeur_2(racine)
print("\n" + "essai")
insertion_par_target(racine, "C")