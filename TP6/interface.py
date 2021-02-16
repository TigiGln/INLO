#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 11:42:01 2021

@author: thierry
"""

from os import path
from tkinter import Button
from tkinter import Entry
from tkinter import Label
from tkinter import Tk
from class_individus import Individu

def creation_view():
    """
    Creation of the directory graphical interface
    """
    win = Tk()
    win.title("Annuaire")
    win.resizable(height = False, width = False)
    widgets_labels = {}
    widgets_entry = {}
    widgets_button = {}
    position_line = 0
    position_col = 0
    champs = ["Nom", "Prénom", "Téléphone", "Adresse", "Ville"]
    buttons = ["Rechercher", "Insérer", "Effacer", "Supprimer", "Sauvegarder/Quitter"]
    for champ in champs:
        lab = Label(win, text = champ)
        widgets_labels[champ] = lab
        lab.grid(row=position_line,column=0)
        entry = Entry(win, text="")
        widgets_entry[champ] = entry
        entry.grid(row=position_line, column=1, columnspan=2, sticky="nesw")
        position_line += 1
    message = Label(win, text="")
    message.grid(row = position_line, column = position_col, columnspan = 3)
    for title in buttons[0:3]:
        button = Button(win, text = title)
        widgets_button[title] = button
        button.grid(row=position_line+1,column=position_col)
        position_col += 1
    position_col = 0
    position_span = 1
    for title in buttons[3:5]:
        button = Button(win, text = title)
        widgets_button[title] = button
        button.grid(row=position_line+2,column=position_col, columnspan = position_span)
        position_col += 1
        position_span += 1

    widgets_entry["Nom"].focus()
    return widgets_button, widgets_entry, widgets_labels, message, champs, win

def file_in_dict():
    """
    Transformation of the data of a file into a dictionary usable by the functions
    """
    dico_individuals = {}
    if path.isfile("annuaire.gtf"):
        with open("annuaire.gtf", "r") as file:
            size = path.getsize(str(file.name))
            if size != 0 :
                for line in file:
                    line = line.strip()
                    line = line.split("\t")
                    if line[0] not in dico_individuals:
                        dico_individuals[line[0]] = Individu(line[0], line[1],
                                                            line[2], line[3],
                                                            line[4])
    else:
        file = open("annuaire.gtf", "w")
        file.close()
    return dico_individuals
