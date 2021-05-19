# -*- coding: utf-8 -*-
"""
Created on Tue May 18 09:37:28 2021

@author: KZemkova
"""


"""
Ukol c. 1 -- PRVOCISLO

Požádej uživatele o zadání celého čísla. Následně urči, zda je toto číslo 
prvočíslo.

Prvočíslo je číslo, které je dělitelné beze zbytku pouze 2 čísly - 1 a sebou 
samotným.

Například 5 je prvočíslo, protože je dělitelná pouze 1 a 5.
Naopak 4 není prvočíslo, protože je dělitelná 1, 2 a 4.
"""

cislo = int(input("Zadej cislo: ")) #uzivatel zada cislo

if cislo > 1: #za prvocisla povazujeme pouze cisla vetsi nez 1
    for i in range(2, cislo):
        if (cislo % i) == 0:
            print("Zadane cislo " + str(cislo) + " neni prvocislo." )
            break #jinak by nam to neskoncilo hned, kdy chceme, ale nakonec by se i ta podminka pro vypsani "je prvocislo" splnila, a to nechci.
    else:
        print("Zadane cislo " + str(cislo) + " je prvocislo.")
else:
    print("Zadane cislo " + str(cislo) + " neni prvocislo.")



"""
Ukol c. 2 -- HADANI CISLA
Napište interaktivní hru, ve které počítač vygeneruje tajné číslo v rozsahu 
1 až 100 (použijte funkci random.randint()). Následně se v cyklu ptejte uživatele,
 aby zadal číslo a vypisujte vždy jestli je zadané číslo nižší nebo vyšší než 
 tajné číslo. Ukončete cyklus v momentě, kdy uživatel trefí tajné číslo.

"""
import random


tajneCislo = random.randint(1, 100)
cisloOdUzivatele = int(input("Tipni si cislo od 1 do 100: "))
while tajneCislo != "cisloOdUzivatele":
    print
    if cisloOdUzivatele < tajneCislo:
        print("Zadane cislo je prilis male.")
        cisloOdUzivatele = int(input("Tipni si cislo od 1 do 100: "))
    elif cisloOdUzivatele > tajneCislo:
        print("Zadane cislo je prilis vysoke.")
        cisloOdUzivatele = int(input("Tipni si cislo od 1 do 100: "))
    else:
        print("Spravne!")
        break
    print

