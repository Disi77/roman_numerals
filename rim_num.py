# Roman Numerals to Arabic Numerals Converter


def kontrola_je_to_rim_cislo(cislo_vstup):
    '''
    Kontrola, zda byl zadán řetězec římských čísel + zda byla dodržena správná syntaxe
    '''
    for x in cislo_vstup:
        if x not in seznam_rim_cisel:
            return cislo_vstup, 'ne'
    for znak in ['I', 'X', 'C']:
        if cislo_vstup.count(znak) > 3:
            return cislo_vstup, 'ne syntaxe'
    for znak in ['V', 'L', 'D']:
        if cislo_vstup.count(znak) > 1:
            return cislo_vstup, 'ne syntaxe'
    spatne = ['VX', 'VL', 'VC', 'VD', 'VM', 'LC', 'LD', 'LM', 'DM', 'IL', 'IC', 'ID', 'IM']
    for znak in spatne:
        if znak in cislo_vstup:
            return cislo_vstup, 'ne syntaxe'
    return cislo_vstup, 'ano'


def jedna_rim_cislice(cislo):
    '''
    Převod římského čísla na arabské v případě, že byl zadán jeden znak.
    '''
    if len(cislo) != 1:
        raise ValueError
    return seznam_rim_cisel[cislo]


def min_dve_rim_cislice(cislo):
    '''
    Převod římského čísla na arabské v případě, že bylo zadáno více znaků.
    POZOR - funguje jen pro čísla, která vznikla po rozpadu původně
    zadaného vstupu od uživatele na pomocné mezivýsledky.
    '''
    pocet_cislic = len(cislo)
    if pocet_cislic <= 1:
        raise ValueError
    if cislo[0] == cislo[1]:
        cislo1 = seznam_rim_cisel[cislo[0]]*(pocet_cislic-1)
        cislo2 = seznam_rim_cisel[cislo[-1]]
    else:
        cislo1 = seznam_rim_cisel[cislo[0]]
        cislo2 = seznam_rim_cisel[cislo[-1]]*(pocet_cislic-1)

    if cislo1 < cislo2:
        return (-1) * cislo1 + cislo2
    else:
        return cislo1 + cislo2


def rozpad_na_mezivysledky(cislo_vstup):
    '''
    Původně zadané číslo se rozpadne na mezivýsledky.
    '''
    seznam_mezivysledky = []
    mezivysledek = ''
    for i in range(len(cislo_vstup)):
        try:
            if seznam_rim_cisel[cislo_vstup[i]] == seznam_rim_cisel[cislo_vstup[i+1]]:
                mezivysledek += cislo_vstup[i]
            elif seznam_rim_cisel[cislo_vstup[i]] < seznam_rim_cisel[cislo_vstup[i+1]]:
                mezivysledek += cislo_vstup[i]
            elif seznam_rim_cisel[cislo_vstup[i]] > seznam_rim_cisel[cislo_vstup[i+1]]:
                mezivysledek += cislo_vstup[i]
                seznam_mezivysledky.append(mezivysledek)
                mezivysledek = ''
        except IndexError:
            mezivysledek += cislo_vstup[i]
            seznam_mezivysledky.append(mezivysledek)
            mezivysledek = ''
    return seznam_mezivysledky


seznam_rim_cisel = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# Vstup od uživatele
while True:
    cislo_vstup = input('Zadej římské číslo: ')
    cislo_vstup = cislo_vstup.upper().strip()
    cislo_vstup, vysledek = kontrola_je_to_rim_cislo(cislo_vstup)
    if vysledek == 'ano':
        break
    if vysledek == 'ne':
        print('Vstup obsahuje znaky, které nejsou římské. Zkus to znovu.')
    else:
        print('Toto není správně zadané římské číslo. Zkus to znovu.')


# Rozpad zadaného římského čísla na "mezivýsledky"
seznam_mezivysledky = rozpad_na_mezivysledky(cislo_vstup)

# Seznam mezivýsledků se projde, každý se vyjádří v arabských čislech a výsledek se sečte
arabske_cislo = 0

for cislo in seznam_mezivysledky:
    if len(cislo) == 1:
        arabske_cislo += jedna_rim_cislice(cislo)
    else:
        arabske_cislo += min_dve_rim_cislice(cislo)

# Výstup
print('Římské číslo {} = Arabské číslo {}'.format(cislo_vstup, arabske_cislo))
