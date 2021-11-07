# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 20:55:05 2021

@author: KristynaZemkova
"""

#importujeme json balicek
import json

#otevreme json soubor a nahrajeme jej do promenne
with open('people.json', encoding='utf-8-sig') as soubor:
    lide = json.load(soubor)

#zalozime si novy seznam
domeny = []
for i in range(len(lide)): # prochazime vsechny polozky
    rozdelene = lide[i]['email'].split('@', 1) # jednotlive polozky rozdelime na znaku '@'
    if rozdelene[1] not in domeny: #vezmeme tu druhou cast po rozdeleni (za znakem '@') a pokud jiz neni v seznamu domeny...
        domeny.append(rozdelene[1]) #priradime ji do seznamu domeny

#vypis seznamu domeny pro kontrolu (nemusi byt)
print(domeny)            

#delka seznamu domeny = POCET UNIKATNICH E-MAILOVYCH DOMEN:
print(len(domeny))             