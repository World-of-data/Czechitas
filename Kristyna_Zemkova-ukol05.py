# -*- coding: utf-8 -*-
"""
Created on Thu May  6 19:35:36 2021

@author: KZemkova
"""

#Domaci ukol c. 1

class Patient:
    
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.vaccinated = False
    
    def vaccine(self):
        self.vaccinated = True
        
    def getInfo(self):
        naockovan = "jeste nebyl"
        if self.vaccinated == True:
            naockovan = "jiz byl"
        return f"Pacient {self.name} s bydlistem {self.address} {naockovan} naockovan proti kovidu."




    
pacient1 = Patient("Lucie", "Veslarska 7, Blansko")
pacient2 = Patient("Pavel", "Stodulky 59, Brno-Zidenice")

print(pacient1.getInfo())
pacient1.vaccine()
print(pacient1.getInfo())

#Domaci ukol c. 2 - priklad c. 3 (Gymnazium)
znamka = input("Zadej znamku z matematiky:")
prumer = input("Zadej prumer vsech znamek z posledniho vysvedceni:")
olympiada = input("Zúčastnil ses okresního kola krajské olympiády? [a/n] ")
olympiada = olympiada.lower() == "a"
if (olympiada or int(znamka) <= 2) and float(prumer) <= 1.8:
    print("Přijmeme vás bez přijímací zkoušky.")
else:
    print("Musíte splnit přijímací zkoušku.")
