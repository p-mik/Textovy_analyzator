"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Petr Mikulky
email: petr.mikulka@gmail.com
discord: p_mik Mik#7555
"""
from task_template import TEXTS

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

# odstraním z listu první dva prvky (user a password)
seznam = seznam[2:]

# naplním z listu slovník tak, že sudá položka je key a lichá value
seznam_uzivatelu = dict() 
for x in range(len(seznam)):
    if x % 2 == 0:
        seznam_uzivatelu[seznam[x]] = seznam[x+1]

# teď přihlašuji uživatele
print("-" * 50)
user = input("Ahoj uživateli! Zadej své uživatelské jméno:\n")

# ověřuji, jestli známe uživatele
if user in seznam_uzivatelu:
    password = input(f"Vítej {user}, jaké je tvé heslo? \n")
else:
    print(f"Jméno {user} není registrováno. Loučím se")
    exit()

# ověřuji správné heslo
print("-" * 50)
if password == seznam_uzivatelu[user]:
    print(f"{user}, vítej v aplikaci!")
    print()
    print(f"Dnes máme k analýze {len(TEXTS)} texty")
    cislo_textu = input(f"Zvol číslo textu, který budeme analyzovat: \n")

else:
    print(f"Heslo nesedí, musíš začít znovu...")
    exit()