#!/usr/bin/python
# -*- coding:utf-8 -*-

mois = [u'janvier', u'février', u'mars', u'avril', u'mai', u'juin', u'juillet', u'août', u'septembre', u'octobre', u'novembre' ,u'décembre']
jours = [u'dimanche',u'lundi',u'mardi',u'mercredi', u'jeudi' , u'vendredi',u'samedi']
types = [u'MUSIQUE CLASSIQUE', u'HUMOUR',u'DANSE', u'CHANSON',u'THÉÂTRE',u'COMÉDIE MUSICALE', u'SPECTACLE MUSICAL',u'CONTE MUSICAL', u'GRAND SPECTACLE', u'GRAND SPECTACLE / CABARET',u'THÉÂTRE / HUMOUR']

class Evenement(object):
    nom = ""
    description = ""
    debut = ""
    fin = ""
    image = ""
    type = ""
    lieu = ""



def proceed(filename):
    f = open(filename)
    for line in f.readlines():
        if line.strip() == "":
            continue
        words = line.split(" ")
        if words[0].isupper():
             if words[0].lower() not in jours and line.strip() not in types:
                print(line)



if __name__ == "__main__":
   proceed('Saison_Culturelle_du_Val_d_Yerres_Abonnements_2014_2015.txt')