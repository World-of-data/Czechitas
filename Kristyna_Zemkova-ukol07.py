# -*- coding: utf-8 -*-
"""
Created on Thu May 20 21:09:25 2021

@author: KZemkova
"""

"""
Ukol - PASAZERI
Autobus mezi Zdebudevsí a Kozoprdy jezdí čtyřikrát denně každý všední den v týdnu. Za poslední týden 
jsme naměřili počty pasažérů pro každou jízdu tam i zpět. Data jsou uložená v souboru pasazeri.txt. 
Jízda vždy obsahuje dvě čísla oddělená čárkou, která udávají počet pasažérů směrem tam a směrem zpět.

1. Napište program, který pro první den vypíše, kolik pasažérů jelo celkem směrem tam a kolik směrem zpět.
2. Nechť váš program vypisuje součty pasažérů ze celý týden, tedy kolik lidí za celý týden jelo směrem tam
 a kolik směrem zpět.
"""

import numpy as np
import pandas as pd

df = pd.read_table('pasazeri.txt', sep=' |,', engine='python', header=None)

table = df.to_numpy()

prvniDenOdjezdy = 0
prvniDenPrijezdy = 0

pocetJizdZaDen = len(table[0])

for i in range(0, pocetJizdZaDen-1, 2):
	prvniDenOdjezdy += table[0,i]
	prvniDenPrijezdy += table[0, i+1]

print("Prvni den - pocet osob, odjezdy: ", prvniDenOdjezdy)
print("Prvni den - pocet osob, prijezdy: ", prvniDenPrijezdy)

celyTydenOdjezdy = []
celyTydenPrijezdy = []

for i in range(0, pocetJizdZaDen-1, 2):
    celyTydenOdjezdy.append(table[:,i])
    celyTydenPrijezdy.append(table[:,i+1])
    
odjezdy = np.array(celyTydenOdjezdy)
prijezdy = np.array(celyTydenPrijezdy)

celkemOdjezdy = np.sum(odjezdy)
celkemPrijezdy = np.sum(prijezdy)

print("Cely tyden - pocet osob, odjezdy: ", celkemOdjezdy)
print("Cely tyden - pocet osob, prijezdy: ", celkemPrijezdy)
