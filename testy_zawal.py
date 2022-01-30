import csv
import math
from reguly import Zbior_Regul, RegLas
from testowania import dokladnosc, dane_statystyczne

kompleks_ogolny = []
with open('ZAWAL/kompleks_ogolny_zawal.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        kompleks_ogolny.append(row)
print(len(kompleks_ogolny))
print(kompleks_ogolny)

training_data = []
with open('ZAWAL/zawal_training.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp = row[-1]
        row.pop(-1)
        row.append(int(temp))
        training_data.append(row)
print(len(training_data))

testing_data = []
with open('ZAWAL/zawal_test.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp = row[-1]
        row.pop(-1)
        row.append(int(temp))
        testing_data.append(row)
print(len(testing_data))
liczba_powtorzen = 15
parametr_m = 5
nowy_zbior = Zbior_Regul(training_data, kompleks_ogolny, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], mmm=parametr_m)

print(training_data[20])
print(nowy_zbior.klasyfikacja(training_data[20]))
print(len(nowy_zbior.zbior_Regul))

[TPR_regul, FPR_regul, Precyzja_regul] = dane_statystyczne(nowy_zbior, testing_data, kompleks_ogolny)
wynik_zbioru = [TPR_regul, FPR_regul, Precyzja_regul, dokladnosc(nowy_zbior, testing_data, kompleks_ogolny)]
print('--M--M--M--M--')
print(parametr_m)
print('_______ZBIOR_________')
print(wynik_zbioru)
print('____________________')
lista_wynikow_lasu = []
for i in range(liczba_powtorzen):
    nowy_las = RegLas(training_data, kompleks_ogolny, 50, RegLasM=parametr_m)
    print('-------------------')
    print(testing_data[20])
    print(nowy_las.klasyfikacja(testing_data[20]))

    print(dokladnosc(nowy_las, testing_data, kompleks_ogolny))
    print(dokladnosc(nowy_zbior, testing_data, kompleks_ogolny))
    [TPR_lasu, FPR_lasu, Precyzja_lasu] = dane_statystyczne(nowy_las, testing_data, kompleks_ogolny)
    wynik_lasu = [TPR_lasu, FPR_lasu, Precyzja_lasu, dokladnosc(nowy_las, testing_data, kompleks_ogolny)]
    print('____________________')
    print(i)
    print(wynik_lasu)
    lista_wynikow_lasu.append(wynik_lasu)

suma = [0, 0, 0, 0]
maks = [0, 0, 0, 0]
mini = [10000, 10000, 10000, 10000]
for wyniki in lista_wynikow_lasu:
    for i, wynik in enumerate(wyniki):
        if wynik > maks[i]:
            maks[i] = wynik
        if wynik < mini[i]:
            mini[i] = wynik
        suma[i] += wynik

srednia = [suma[0]/liczba_powtorzen, suma[1]/liczba_powtorzen, suma[2]/liczba_powtorzen, suma[3]/liczba_powtorzen]
odchylenie = [0, 0, 0, 0]
suma = [0, 0, 0, 0]
for wyniki in lista_wynikow_lasu:
    for i, wynik in enumerate(wyniki):
        suma[i] += (wynik-srednia[i])*(wynik-srednia[i])

for i in range(4):
    odchylenie[i] = math.sqrt(suma[i]/liczba_powtorzen)


print('--M--M--M--M--')
print(parametr_m)
print("______ODCHYLENIE")
print(odchylenie)
print("______SREDNIA")
print(srednia)
print("______MAKS")
print(maks)
print("______MINI")
print(mini)
