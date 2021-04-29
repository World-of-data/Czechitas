# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 19:38:47 2021

@author: KZemkova
"""
#DOMACI UKOL
#Napiš funkce monthOfBirth, která bude mít jeden parametr - rodné číslo. 
#Funkce ze zadaného rodného čísla určí měsíc narození, které vrátí jako výstup. 
#Nezapomeň, že pro ženy je k měsíci připočtena hodnota 50.

#Příklad: Pro hodnotu 9207054439 vrátí 7. Pro hodnotu 9555125899 vrátí 5.

def monthOfBirth(rodne_cislo):
    mesic = int(str(rodne_cislo)[2:4])
    if mesic >=12:
        return mesic-50
    else:
        return mesic