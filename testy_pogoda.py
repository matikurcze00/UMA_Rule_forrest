import csv
import math
from reguly import Zbior_Regul, RegLas
from testowania import dokladnosc, dane_statystyczne

kompleks_ogolny = []
with open('POGODA/kompleks_ogolny_pogoda.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        kompleks_ogolny.append(row)
print(len(kompleks_ogolny))
print(kompleks_ogolny)

training_data = []
with open('POGODA/pogoda_training.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp = row[-1]
        row.pop(-1)
        row.append(int(temp))
        training_data.append(row)
print(len(training_data))

testing_data = []
with open('POGODA/pogoda_test.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp = row[-1]
        row.pop(-1)
        row.append(int(temp))
        testing_data.append(row)
print(len(testing_data))
for par_sze in [10,50]:

  f = open('Pogoda_testy_para_sze.txt', 'a')

  liczba_powtorzen = 7
  parametr_m = 2
  szer = par_sze

  f.writelines('--Liczba Drzew--')
  f.write('\n')
  f.writelines(str(szer))
  f.write('\n')


  nowy_zbior = Zbior_Regul(training_data, kompleks_ogolny, [0, 1, 2, 3, 4, 5, 6, 7, 8,9], mmm=parametr_m)
  print(len(nowy_zbior.zbior_Regul))

  [TPR_regul, FPR_regul, Precyzja_regul] = dane_statystyczne(nowy_zbior, testing_data, kompleks_ogolny)
  wynik_zbioru = [TPR_regul, FPR_regul, Precyzja_regul, dokladnosc(nowy_zbior, testing_data, kompleks_ogolny)]
  print('--M--M--M--M--')
  print(parametr_m)
  print('_______ZBIOR_________')
  print(wynik_zbioru)
  print('____________________')
  f.writelines('_______ZBIOR_________')
  f.write('\n')
  f.writelines(str(wynik_zbioru))
  f.write('\n')
  lista_wynikow_lasu = []
  for i in range(liczba_powtorzen):
      nowy_las = RegLas(training_data, kompleks_ogolny, szerokosc=szer, RegLasM=parametr_m)
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

  f.writelines('_______LAS________')
  f.write('\n')
  f.writelines("______ODCHYLENIE")
  f.write('\n')
  f.writelines(str(odchylenie))
  f.write('\n')
  f.writelines("______SREDNIA")
  f.write('\n')
  f.writelines(str(srednia))
  f.write('\n')
  f.writelines("______MAKS")
  f.write('\n')
  f.writelines(str(maks))
  f.write('\n')
  f.writelines("______MINI")
  f.write('\n')
  f.writelines(str(mini))
  f.write('\n')
  f.writelines('')
  f.write('\n')
  f.writelines('')
  f.write('\n')

  f.close()

for m in [1,5,10]:

  f = open('Pogoda_testy_para_m.txt', 'a')

  liczba_powtorzen = 7
  parametr_m = m
  szer = 50

  f.writelines('--M-M-M-M--')
  f.write('\n')
  f.writelines(str(parametr_m))
  f.write('\n')


  nowy_zbior = Zbior_Regul(training_data, kompleks_ogolny, [0, 1, 2, 3, 4, 5, 6, 7, 8,9], mmm=parametr_m)
  print(len(nowy_zbior.zbior_Regul))

  [TPR_regul, FPR_regul, Precyzja_regul] = dane_statystyczne(nowy_zbior, testing_data, kompleks_ogolny)
  wynik_zbioru = [TPR_regul, FPR_regul, Precyzja_regul, dokladnosc(nowy_zbior, testing_data, kompleks_ogolny)]
  print('--M--M--M--M--')
  print(parametr_m)
  print('_______ZBIOR_________')
  print(wynik_zbioru)
  print('____________________')
  f.writelines('_______ZBIOR_________')
  f.write('\n')
  f.writelines(str(wynik_zbioru))
  f.write('\n')
  lista_wynikow_lasu = []
  for i in range(liczba_powtorzen):
      nowy_las = RegLas(training_data, kompleks_ogolny, szerokosc=szer, RegLasM=parametr_m)
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

  f.writelines('_______LAS________')
  f.write('\n')
  f.writelines("______ODCHYLENIE")
  f.write('\n')
  f.writelines(str(odchylenie))
  f.write('\n')
  f.writelines("______SREDNIA")
  f.write('\n')
  f.writelines(str(srednia))
  f.write('\n')
  f.writelines("______MAKS")
  f.write('\n')
  f.writelines(str(maks))
  f.write('\n')
  f.writelines("______MINI")
  f.write('\n')
  f.writelines(str(mini))
  f.write('\n')
  f.writelines('')
  f.write('\n')
  f.writelines('')
  f.write('\n')

  f.close()