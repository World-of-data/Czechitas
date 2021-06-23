# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 10:59:22 2021

@author: KZemkova

Domaci ukol - adresy stranek

Adresy webových stránek zpravidla začínají záhadným shlukem písmen http:// nebo https://. Například náš web 
najdete pod adresou https://kodim.cz. Zkrátka HTTP nebo HTTPS je ve skutečnosti označení protokolu, což je nějaký 
popis toho, jak by měla vypadat komunikace mezi dvěma zařízeními. Standardního tvaru můžeme využít, abychom z textu 
vytáhli všechny adresy. Napiš program, který z proměnné emailSRadami vytáhne všechny webové stránky, které jsou tam
 zmíněny.
"""

emailSRadami = """
Ahoj,
posílám ti pár tipů, kam se podívat. https://realpython.com nabízí spoustu článků i kurzů. http://docs.python.org 
nabízí tutoriál i rozsáhlou dokumentaci. http://www.learnpython.org nabízí hezky strukturovaný kurz pro začátečníky,
 rozebírá ale i nějaká pokročilejší témata. https://www.pluralsight.com je placený web, který ale kvalitou kurzů 
 víceméně nemá konkurenci. Určitě ale sleduj i web https://www.czechitas.cz.
"""

import re

webovkaRegex = re.compile(r"((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)")
webovky = webovkaRegex.findall(emailSRadami) 
print([web[0] for web in webovky])

