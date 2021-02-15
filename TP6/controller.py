#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 12:22:29 2021

@author: thierry
"""


#from re import match
from tkinter import Label
from tkinter import Tk
from tkinter.messagebox import askquestion
from tkinter.messagebox import showwarning
# from interface import Message
# from interface import widgets_entry
# from interface import dico_individus


def insert_individus():
    tel = compile('^0[1-9][0-9]{8}$')
    if widgets_entry["Nom"].get() != "" and widgets_entry["Prénom"].get() != "" \
    and widgets_entry["Téléphone"].get() != "" and widgets_entry["Adresse"].get() != "" \
    and widgets_entry["Ville"].get() != "":
        if tel.match(widgets_entry["Téléphone"].get()):
            name = widgets_entry["Nom"].get().upper()
            object_individu = Individu(name, widgets_entry["Prénom"].get(),
                         widgets_entry["Téléphone"].get(), widgets_entry["Adresse"].get(), 
                         widgets_entry["Ville"].get())
            if name not in dico_individus:
                dico_individus[name] = object_individu
                Message["text"] =  "L'individu " + name + " est ajouter à votre carnet d'adresse"
                efface()
            else:
                msgbox = askquestion(title='Error', message="Ce nom existe déjà,\
                                     voulez-vous le remplacer", 
                                     icon="error")
                if msgbox == 'yes':
                    dico_individus[name] = object_individu
                    Message["text"] =  "L'individu " + name + " est ajouter à votre carnet d'adresse"
                    efface()
        else:
            showwarning(title='Error', message="Le numéro de téléphone est incorrecte")
    else:
        showwarning(title='Error', message="Merci de remplir tous les champs")
    widgets_entry["Nom"].focus()
    return dico_individus
def search_individus():
    name = widgets_entry["Nom"].get().upper()
    #firstname = str(widgets_entry["Prénom"].get())
    if name in dico_individus:
        win2 = Tk()
        win2.title("Personne trouvée")
        win2.resizable(height = False, width = False)
        liste = [dico_individus[name].name, dico_individus[name].firstname, 
                 dico_individus[name].phone,dico_individus[name].address, 
                 dico_individus[name].city]
        position_line = 0
        for word in champs:
            label = Label(win2, text=word + ": ")
            label.grid(row=position_line, column=0)
            position_line += 1
        position_line = 0
        for info in liste:
            information = Label(win2, text= info)
            information.grid(row=position_line, column=1, columnspan=2)
            position_line += 1
    else:
        showwarning(title='Error', message="Il n'existe pas d'individus de ce nom")
def efface():
    length = len(champs)
    global widgets_entry
    while length > 0:
        widgets_entry[champs[length-1]].delete(0, "end")
        length -= 1
    #Message["text"] = ""
def delete():
    name = widgets_entry["Nom"].get().upper()
    if name in dico_individus:
        del dico_individus[name]
        Message["text"] = "L'individus " + name + " a bien été effacé du carnet d'adresse."

def save_and_quit():
   with open( "annuaire.txt", 'w') as file:
       for keys, values in dico_individus.items():
            file.write(keys + "\t" + values.firstname + "\t" + values.phone + 
                       "\t" + values.address + "\t" + values.city + "\n")
       win.destroy()
    

 
