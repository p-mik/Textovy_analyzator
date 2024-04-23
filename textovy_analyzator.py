"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Petr Mikulky
email: petr.mikulka@gmail.com
discord: p_mik Mik#7555
"""
from task_template import TEXTS
from seznam_uzivatelu import seznam_uzivatelu

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