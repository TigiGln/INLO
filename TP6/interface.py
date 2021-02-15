#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 11:42:01 2021

@author: thierry
"""

from os import path
import re
from tkinter import Button
from tkinter import Entry
from tkinter import Label
from tkinter import Tk
from tkinter.messagebox import askquestion
from tkinter.messagebox import showwarning
from class_individus import Individu
# from controller import *
# # from controller import insert_individus
# # from controller import save_and_quit
# # from controller import search_individus
# # from controler import delete
# # from controler import efface

def insert_individus():
    """
    Allows you to insert an individual
    """
    phone = re.compile('^0[1-9][0-9]{8}$')
    if widgets_entry["Nom"].get() != "" and widgets_entry["Prénom"].get() != "" \
    and widgets_entry["Téléphone"].get() != "" and widgets_entry["Adresse"].get() != "" \
    and widgets_entry["Ville"].get() != "":
        if phone.match(widgets_entry["Téléphone"].get()):
            name = widgets_entry["Nom"].get().upper()
            object_individuals = Individu(name, widgets_entry["Prénom"].get(),
                         widgets_entry["Téléphone"].get(), widgets_entry["Adresse"].get(),
                         widgets_entry["Ville"].get())
            if name not in dico_individuals:
                dico_individuals[name] = object_individuals
                Message["text"] =  "L'individus " + name + " est ajouter à votre carnet d'adresse"
                efface()
            else:
                msgbox = askquestion(title='Error', message="Ce nom existe déjà,\
                                     voulez-vous le remplacer",
                                     icon="error")
                if msgbox == 'yes':
                    dico_individuals[name] = object_individuals
                    Message["text"] =  "L'individu " + name + \
                                        " est ajouter à votre carnet d'adresse"
                    efface()
        else:
            showwarning(title='Error', message="Le numéro de téléphone est incorrecte")
    else:
        showwarning(title='Error', message="Merci de remplir tous les champs")
    widgets_entry["Nom"].focus()

def search_individus():
    """
    Allows you to search for an individual in the address book
    """
    name = widgets_entry["Nom"].get().upper()
    if name in dico_individuals:
        win2 = Tk()
        win2.title("Personne trouvée")
        win2.resizable(height = False, width = False)
        liste = [dico_individuals[name].name, dico_individuals[name].firstname,
                 dico_individuals[name].phone,dico_individuals[name].address,
                 dico_individuals[name].city]
        position_line = 0
        for words in champs:
            label = Label(win2, text=words + ": ")
            label.grid(row=position_line, column=0)
            position_line += 1
        position_line = 0
        for info in liste:
            information = Label(win2, text= info)
            information.grid(row=position_line, column=1, columnspan=2)
            position_line += 1
    else:
        showwarning(title='Error', message="Il n'existe pas d'individus de ce nom")
    efface()
    widgets_entry["Nom"].focus()

def efface():
    """
    Allows you to empty all input fields
    """
    length = len(champs)
    while length > 0:
        widgets_entry[champs[length-1]].delete(0, "end")
        length -= 1
    #Message["text"] = ""

def delete():
    """
    Allows you to delete an individual
    """
    name = widgets_entry["Nom"].get().upper()
    if name in dico_individuals:
        del dico_individuals[name]
        Message["text"] = "L'individus " + name + " a bien été effacé du carnet d'adresse."

def save_and_quit():
    """
    Allows you to save individuals to a file and exit the application
    """
    with open( "annuaire.gtf", 'w') as phone_book:
        for keys, values in dico_individuals.items():
            phone_book.write(keys + "\t" + values.firstname + "\t" + values.phone +
                       "\t" + values.address + "\t" + values.city + "\n")
        win.destroy()

win = Tk()
win.title("Annuaire")
win.resizable(height = False, width = False)

champs = ["Nom", "Prénom", "Téléphone", "Adresse", "Ville"]
buttons = ["Rechercher", "Insérer", "Effacer", "Supprimer", "Sauvegarder/Quitter"]

widgets_labels = {}
widgets_entry = {}
widgets_button = {}
dico_individuals = {}
POSITION_LINE = 0
POSITION_COL = 0

for champ in champs:
    lab = Label(win, text = champ)
    widgets_labels[champ] = lab
    lab.grid(row=POSITION_LINE,column=0)
    entry = Entry(win, text="")
    widgets_entry[champ] = entry
    entry.grid(row=POSITION_LINE, column=1, columnspan=2, sticky="nesw")
    POSITION_LINE += 1
Message = Label(win, text="")
Message.grid(row = POSITION_LINE, column = POSITION_COL, columnspan = 3)
for title in buttons[0:3]:
    button = Button(win, text = title)
    widgets_button[title] = button
    button.grid(row=POSITION_LINE+1,column=POSITION_COL)
    POSITION_COL += 1
POSITION_COL = 0
POSITION_SPAN = 1
for title in buttons[3:5]:
    button = Button(win, text = title)
    widgets_button[title] = button
    button.grid(row=POSITION_LINE+2,column=POSITION_COL, columnspan = POSITION_SPAN)
    POSITION_COL += 1
    POSITION_SPAN += 1

widgets_entry["Nom"].focus()
widgets_button["Sauvegarder/Quitter"].config(command = save_and_quit)
widgets_button["Insérer"].config(command = insert_individus)
widgets_button["Rechercher"].config(command = search_individus)
widgets_button["Effacer"].config(command = efface)
widgets_button["Supprimer"].config(command = delete)

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

win.mainloop()
