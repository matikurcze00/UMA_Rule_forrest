import itertools
import copy
import collections
import random
import math

def koniunkcja_selektorow(selektor_1, selektor_2):
    selektor = [i for i in selektor_1 if i in selektor_2]
    return selektor


def koniunkcja_kompleksow(kompleks_1, kompleks_2):
    kompleks = []
    for i in range(len(kompleks_1)):
        kompleks.append(koniunkcja_selektorow(kompleks_1[i], kompleks_2[i]))
    if kompleks.count([]) > 0:
        kompleks = [[] for x in kompleks]
    return kompleks


def koniunkcja_zbiorow_kompleksow(zbior_1, zbior_2):
    zbior = []
    for kompleks_zbior_1 in zbior_1:
        for kompleks_zbior_2 in zbior_2:
            zbior.append(koniunkcja_kompleksow(kompleks_zbior_1, kompleks_zbior_2))
    final_zbior = [i for n, i in enumerate(zbior) if i not in zbior[:n]]
    return final_zbior


def utworz_kompleks_atomowy_z_selektora(selektor_ogolny, kompleks_ogolny, pozycja):
    zbior_kompleksow = []
    all_combinations = []
    for r in range(1, len(selektor_ogolny)):
        combinations_object = itertools.combinations(selektor_ogolny, r)
        combinations_list = list(combinations_object)
        all_combinations += combinations_list
    all_combinations = [list(x) for x in all_combinations]
    for selektor in all_combinations:
        kompleks = copy.copy(kompleks_ogolny)
        kompleks[pozycja] = selektor
        zbior_kompleksow.append(kompleks)
    return zbior_kompleksow


def utworz_kompleksy_atomowe(kompleks_ogolny):
    zbior_kompleksow_atomowych = []
    i = 0
    for selektor in kompleks_ogolny:
        zbior_kompleksow_atomowych += utworz_kompleks_atomowy_z_selektora(selektor, kompleks_ogolny, i)
        i += 1
    return zbior_kompleksow_atomowych


def czy_kompleks_pokrywa_przyklad(kompleks, przyklad):
    i = 0
    for selektor in przyklad:
        if selektor not in kompleks[i]:
            return False
        i += 1
        if i == len(przyklad) - 1:
            break
    return True


def liczba_przykladow_pokrywanych_przez_kompleks(zbior_przykladow, kompleks):
    liczba = 0
    liczba_o_klasie_dom = 0
    klasa = 1
    for przyklad in zbior_przykladow:
        if czy_kompleks_pokrywa_przyklad(kompleks, przyklad):
            liczba += 1
            liczba_o_klasie_dom += przyklad[len(przyklad)-1]
    if liczba/2 > liczba_o_klasie_dom:
        liczba_o_klasie_dom = liczba - liczba_o_klasie_dom
        klasa = 0
    return liczba, liczba_o_klasie_dom, klasa


def liczby_przykladow_dla_statystycznej(zbior_przykladow, kompleks):
    liczba_pokrytych = 0
    liczba_o_klasie_1 = 0
    liczba_o_klasie_0 = 0
    liczba_pokrytych_o_klasie_1 = 0
    for przyklad in zbior_przykladow:
        liczba_o_klasie_1 += przyklad[len(przyklad)-1]
        if czy_kompleks_pokrywa_przyklad(kompleks, przyklad):
            liczba_pokrytych += 1
            liczba_pokrytych_o_klasie_1 += przyklad[len(przyklad)-1]
    liczba_pokrytych_o_klasie_0 = liczba_pokrytych - liczba_pokrytych_o_klasie_1
    liczba_o_klasie_0 = len(przyklad) - liczba_o_klasie_1
    return liczba_pokrytych, liczba_o_klasie_1, liczba_o_klasie_0, liczba_pokrytych_o_klasie_1, liczba_pokrytych_o_klasie_0


def jakosc_kompleksu_na_zbiorze(kompleks, zbior_przykladow, m=2, liczebnosc_C=2):
    [liczba_przyk_pok, liczba_przyk_o_k_d, _] = liczba_przykladow_pokrywanych_przez_kompleks(zbior_przykladow, kompleks)
    return (liczba_przyk_o_k_d + (m/liczebnosc_C))/(liczba_przyk_pok + m)


def edk_do_stat(Pk, Pd, P):
    return (Pk*Pd)/P


def ulamek_do_stat(Pdk, edk):
    return ((Pdk-edk)*(Pdk-edk))/edk


def czy_kompleks_statystycznie_istotny(kompleks, zbior_przykladow):
    theta = 6.6349
    [Pk, P0, P1, P0k, P1k] = liczby_przykladow_dla_statystycznej(zbior_przykladow, kompleks)
    P = len(zbior_przykladow)
    statystyka = (ulamek_do_stat(P0k, edk_do_stat(Pk, P0, P)))+(ulamek_do_stat(P1k, edk_do_stat(Pk, P1, P)))
    if statystyka > theta:
        return True
    return False


def znajdz_kompleks_cn2(z_T, z_P, zbior_atomowych, kompleks_ogolny, m=5):
    S = [kompleks_ogolny]
    k_wybrany = kompleks_ogolny

    def jakosc(kompl):
        return jakosc_kompleksu_na_zbiorze(kompl, z_P)

    while S != []:
        S_zapas = koniunkcja_zbiorow_kompleksow(S, zbior_atomowych)
        S_zapas = [i for i in S_zapas if i not in S]
        S_zapas = [i for i in S_zapas if i not in [[[], [], [], []]]]
        for kompleks in S_zapas:
            if jakosc_kompleksu_na_zbiorze(kompleks, z_P) > jakosc_kompleksu_na_zbiorze(k_wybrany, z_P):
                # if czy_kompleks_statystycznie_istotny(kompleks, z_P):
                    k_wybrany = copy.copy(kompleks)
        S_zapas.sort(reverse=True, key=jakosc)
        if len(S_zapas) > 0:
            S = [S_zapas[i] for i in range(min(m, len(S_zapas)))]
        else:
            S = S_zapas
    return k_wybrany


def usun_przyklady_pokrywane_przez_kompleks(z_przykl, kompleks):
    zbior = []
    zbior = [przyk for przyk in z_przykl if not czy_kompleks_pokrywa_przyklad(kompleks, przyk)]
    return zbior


def skroc_kompleks_ogolny(kompleks_ogolny, header):
    nowy_kompleks_ogolny = []
    for kolumna in header:
        nowy_kompleks_ogolny.append(kompleks_ogolny[kolumna])
    return nowy_kompleks_ogolny


def rozszerz_kompleks(kompleks, kompleks_ogolny, header):
    nowy_kompleks = []
    kopia_header = copy.copy(header)
    i = 0
    flaga = 1
    for kolumna in range(len(kompleks_ogolny)):
        if flaga:
            if kolumna == kopia_header[0]:
                nowy_kompleks.append(kompleks[i])
                i += 1
                kopia_header.remove(kolumna)
                if len(kopia_header) < 1:
                    flaga = 0
            else:
                nowy_kompleks.append(kompleks_ogolny[kolumna])
        else:
            nowy_kompleks.append(kompleks_ogolny[kolumna])
    return nowy_kompleks


def sekwencyjne_pokrywanie(zbior_T, kompleks_ogolny_skrocony, kompleks_ogolny, header):
    zbior_Regul = []
    zbior_P = copy.copy(zbior_T)
    zbior_atom = utworz_kompleksy_atomowe(kompleks_ogolny_skrocony)
    while zbior_P != []:
        kompleks = znajdz_kompleks_cn2(zbior_T, zbior_P, zbior_atom, kompleks_ogolny_skrocony,  m=1)
        [_, _, klasa] = liczba_przykladow_pokrywanych_przez_kompleks(zbior_P, kompleks)
        zbior_Regul.append((rozszerz_kompleks(kompleks, kompleks_ogolny, header), klasa))
        zbior_P = usun_przyklady_pokrywane_przez_kompleks(zbior_P, kompleks)
    return zbior_Regul


class Zbior_Regul:
    def __init__(self, zbior_T, kompleks_ogolny, header):
        self.zbior_Regul = sekwencyjne_pokrywanie(zbior_T, skroc_kompleks_ogolny(kompleks_ogolny, header), kompleks_ogolny, header)
        self.kompleks_ogolny = kompleks_ogolny

    def klasyfikacja(self, przyklad):
        for regula in self.zbior_Regul:
            if czy_kompleks_pokrywa_przyklad(regula[0], przyklad):
                return regula[1]



def RegDrzewo(zbior_T, kompleks_ogolny):
  dlugosc_kompleksu = len(kompleks_ogolny)
  dlugosc_zbioru = len(zbior_T)

  nowy_kompleks = []
  nowy_kompleks =  random.sample(range(dlugosc_kompleksu-1),math.ceil(math.sqrt(dlugosc_kompleksu))-1)
  nowy_kompleks.sort()
  nowy_kompleks.append(dlugosc_kompleksu-1)
  
  
  nowy_trenujacy=[]
  for dane in range(dlugosc_zbioru):
    temp_wiersz = []
    wiersz = random.randrange(dlugosc_zbioru)
    for kompleks in nowy_kompleks:
      temp_wiersz.append(zbior_T[wiersz][kompleks])
    temp_wiersz.append(zbior_T[wiersz][dlugosc_kompleksu])
    nowy_trenujacy.append(temp_wiersz)


  Drzewo = Zbior_Regul(nowy_trenujacy, kompleks_ogolny, nowy_kompleks)
  return Drzewo

def RegLas(dane_T, kompleks_ogolny, szerokosc):
  Forest = []
  for t in range(szerokosc):
    Forest[t]=RegDrzewo(dane_T,kompleks_ogolny)
  return Forest
