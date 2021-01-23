#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
un peu de documentation
"""

__author__ = 'Thierry Galliano'



def is_valid(adn_str):
    counter = 0
    for letter in adn_str.lower():
        if letter == "a" or letter == "t" or letter == "c" or letter == "g":
            counter += 1
    if counter == len(adn_str) and counter != 0:
        return True
        


def get_valid_adn(prompt='chaîne : '):
    while not is_valid(prompt):
        prompt = input("Entrez une sequence d'ADN : \n")
    print("Votre séquence d'ADN est : " + str(prompt))


