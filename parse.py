#!/usr/bin/python
# -*- coding:utf-8 -*-

from datetime import datetime, date, time, timedelta
from django.template import defaultfilters
from
import os

mois = [u'janvier', u'février', u'mars', u'avril', u'mai', u'juin', u'juillet', u'août', u'septembre', u'octobre', u'novembre' ,u'décembre']
jours = [u'dimanche',u'lundi',u'mardi',u'mercredi', u'jeudi' , u'vendredi',u'samedi']
types = [u'MUSIQUE CLASSIQUE', u'HUMOUR',u'DANSE', u'CHANSON',u'THÉÂTRE',u'COMÉDIE MUSICALE', u'SPECTACLE MUSICAL',
         u'CONTE MUSICAL', u'GRAND SPECTACLE', u'GRAND SPECTACLE / CABARET',u'THÉÂTRE / HUMOUR']

eventlist = list()

class evenement(object):

    def __init__(self):
        self.nom = ""
        self.description = ""
        self.debut = ""
        self.fin = ""
        self.image = ""
        self.type = ""
        self.lieu = ""
        self.copyrightimg=""



def proceed(filename):
    f = open(filename)
    event = evenement()
    for line in f.readlines():
        line = unicode(line, encoding="utf-8")
        if u"©" in line:
            event.copyrightimg = line.strip()

        if line.strip() == u"" or u"©" in line :
            continue
        words = line.split(" ")
        charlower = u"".join([c for c in line if c.islower()])

        if words[0].isupper() or words[0] is u"«" or words[0] is u"&" :
             if words[0].lower() not in jours and line.strip() not in types:
                if u"€" not in line and u"/" not in line and event.description is "" :
                    event.nom = event.nom+u" " + line
                    event.nom = event.nom.strip().title()
        if len(words) > 1 and charlower.islower():
            event.description = event.description+" " + line
            event.description = event.description.strip()
        if event.description is not "" and u"€" not in line and words[0].lower() not in jours:
            if words[0].isupper() and line.strip() not in types:
                event.description = event.description+"\n" + line.title()
                event.description = event.description.strip()

        if line.strip() in types:
            line = line.split(u"/")[0]
            event.type = line.strip().capitalize()

        if words[0].lower() in jours:
            jour, lieu = line.split(u"/")
            event.lieu = lieu.strip()
            numjour = words[1]
            nummois = 99
            if numjour == u"1ER":
                numjour = 1
            numjour = int(numjour)
            for i, m in enumerate(mois):
                if words[2].lower() in m :

                    nummois = int(i)+1
                    break
            numannee = 0
            if nummois > 6:
                numannee = 2014
            else:
                numannee = 2015
            mydate = date(numannee, nummois,numjour)
            heure, minutes = words[4].split(u'H')
            heure = int(heure)
            if minutes == "":
                minutes = 0
            else:
                minutes = int(minutes)
            mytime = time(heure, minutes)
            event.debut = datetime.combine(mydate, mytime)





        if u"[" in line and u"]" in line :

            heures, minutes = words[3].split(u"H")
            if minutes == u"":
                minutes = 0
            else:
                minutes = int(minutes)
            heures = int(heures)
            delta = timedelta(hours=heures, minutes=minutes)

            event.fin = event.debut + delta
            print(u"-------------------------------------------")
            print(event.nom)
            print(event.description)
            print(event.debut)
            print(event.fin)
            print(event.type)
            print(event.lieu)
            print(event.copyrightimg)
            eventlist.append(event)
            event = evenement()


def imgtraitement():
    mypath = os.path.abspath(os.path.split(__file__)[0])
    imgpath = os.path.join(mypath,"img-test")
    for i, event in enumerate(eventlist):
        img = os.path.join( imgpath, str(i)+".jpg")
        imgname = os.path.join(imgpath,defaultfilters.slugify(event.nom)+".jpg")
        command = u"convert "+img+u" -fill white -gravity southeast -annotate 0 '"+event.copyrightimg+u"' "+imgname
        #shlex ne supporte pas le caractère copyright et il a bien raison
        #du coup on récupère les commandes et on les lance dans le terminal
        print(command)
    return 1






if __name__ == "__main__":
   proceed('Saison_Culturelle_du_Val_d_Yerres_Abonnements_2014_2015.txt')
   imgtraitement()
