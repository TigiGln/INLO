#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 11:40:57 2021

@author: thierry
"""

class Individu:
    def __init__(self, nom, prenom, tel, adresse, ville):
        self.name = nom
        self.firstname = prenom
        self.phone = tel
        self.address = adresse
        self.city = ville
    def __str__(self):
        return self.name + " " + " " + self.firstname