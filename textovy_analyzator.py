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

# Kontrola, zda klient zvolil číslo a text v rozmezí

if not cislo_textu.isdigit() or int(cislo_textu) < 1 or int(cislo_textu) > 3:
    print(f"Bohužel jsi nezvolil v požadovaném rozmezí. Končíme...")
    exit()
else:
    cislo_textu = int(cislo_textu)

# Příprava proměnných

pocet_slov = 0
zacina_velkym = 0
vse_velkym = 0
vse_malym = 0
pocet_cisel = 0
suma_cisel = 0
delka_slov = {}
    
#ITERACE NAD VYBRANÝM TEXTEM
for slovo in TEXTS[cislo_textu - 1].split():
    # POČET SLOV
    pocet_slov += 1

    # POČET SLOV ZAČÍNAJÍCÍCH VELKÝM PÍSMENEM
    if slovo.istitle():
        zacina_velkym += 1
    
    # POČET SLOV PSANÝCH VELKÝMI PÍSMENY
    elif slovo.isupper():
        vse_velkym += 1
    
    # POČET SLOV PSANÝCH VELKÝMI PÍSMENY
    elif slovo.islower():
        vse_malym += 1
    
    # POČET ČÍSEL
    elif slovo.isdigit():
        pocet_cisel += 1
    # SUMA ČÍSEL
        suma_cisel += int(slovo)
print()
print("-" * 50)
print(f"Počet slov v textu: {pocet_slov}")
print(f"Počet slov začínajících velkým písmenem: {zacina_velkym}")
print(f"Počet slov psaných pouze velkými písmeny: {vse_velkym}")
print(f"Počet slov psaných pouze malými písmeny: {vse_malym}")
print(f"Počet čísel v textu: {pocet_cisel}")
print(f"Součet čísel v textu: {suma_cisel}")
print("-" * 50)

# GRAF
# připravit si proměnnou
hodnoty_grafu = {}
# iterovat přes text ke změření slov

for delka_slova in TEXTS[cislo_textu - 1].split():
    delka_slova = delka_slova.rstrip(".,!?:;")
    hodnoty_grafu[len(delka_slova)] = hodnoty_grafu.get(len(delka_slova), 0) + 1
# vykreslit graf pomocí formátovacích znaků

print("{:>6} |".format("DÉLKA"), "{:^17}".format("VÝSKYTY"), "| {:<6}".format("POČET"))
print("-" * 50)

for key in sorted(hodnoty_grafu.keys()):
    print("{:>6} |".format(key), "{:<17}".format("*" * hodnoty_grafu[key]), "| {:<6}".format(hodnoty_grafu[key]))

print("-" * 50)

print(hodnoty_grafu)