# -*- coding: utf-8 -*-
"""
Created on Fri May 28 11:27:09 2021

@author: KZemkova
"""


"""
ZADANI:
Pohlédněte na následující reprezentaci receptu:

{
  'nazev': 'Batáty se šalvějí a pancettou',
  'narocnost': 'stredni',
  'doba': 30,
  'ingredience': [
    ['batát', '1', '15 kč'],
    ['olivový olej', '2 lžíce', '2 kč'],
    ['pancetta', '4-6 plátků', '21 kč'],
    ['přepuštěné máslo', '2 lžíce', '5 kč'],
    ['mletý černý pepř', '1/2 lžičky', '0.5 kč'],
    ['sůl', '1/2 lžičky', '0.1 kč'],
    ['muškátový oříšek', 'špetka', '1 kč'],
    ['česnek', '2 stroužky', '1 kč'],
    ['šalvějové lístky', '20-25', '12 kč']
  ]
}
Uložte si tuto strukturu do proměnné recept na začátek nového programu. 
Vypište pomocí funkce print kolik bude celé jídlo stát korun zaokrouhlené na 
celé koruny nahoru.
"""

recept = {
  'nazev': 'Batáty se šalvějí a pancettou',
  'narocnost': 'stredni',
  'doba': 30,
  'ingredience': [
    ['batát', '1', '15 kč'],
    ['olivový olej', '2 lžíce', '2 kč'],
    ['pancetta', '4-6 plátků', '21 kč'],
    ['přepuštěné máslo', '2 lžíce', '5 kč'],
    ['mletý černý pepř', '1/2 lžičky', '0.5 kč'],
    ['sůl', '1/2 lžičky', '0.1 kč'],
    ['muškátový oříšek', 'špetka', '1 kč'],
    ['česnek', '2 stroužky', '1 kč'],
    ['šalvějové lístky', '20-25', '12 kč']
  ]
}

nazevReceptu = recept['nazev'] 
suroviny = len(recept['ingredience'])
ceny = []
for i in range(0, suroviny):
    cena = recept['ingredience'][i][-1]
    ceny.append(float(cena.replace(' kč', '')))
celkovaCena = round(sum(ceny))
print(f"Nakoupit suroviny na {nazevReceptu} te bude stat celkem {celkovaCena} Kc.")


