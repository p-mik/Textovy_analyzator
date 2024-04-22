"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Petr Mikulky
email: petr.mikulka@gmail.com
discord: p_mik Mik#7555
"""
from task_template import TEXTS

#print(str(TEXTS[0]))

# mám seznam uživatelů jako víceřádkový string
registrovani_uzivatele = """
+------+-------------+
| user |   password  |
+------+-------------+
| bob  |     123     |
| ann  |   pass123   |
| mike | password123 |
| liz  |   pass123   |
+------+-------------+
"""

# z víceřádkového stringu vytvořím slovník tak, že:

# rozdělím string na jednotlivá slova do listu
seznam = registrovani_uzivatele.split() 

# odstraním položky, které nejsou alfanumerické
for prvek in seznam.copy(): 
    if not prvek.isalnum():
        seznam.remove(prvek)

# naplním z listu slovník tak, že sudá položka je key a lichá value
seznam_uzivatelu = dict() 
for x in range(len(seznam)):
    if x % 2 == 0:
        seznam_uzivatelu[seznam[x]] = seznam[x+1]

print(str(seznam_uzivatelu))

#print(seznam)
