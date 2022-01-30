import csv
import math
import numpy
import sklearn
from numpy import mean
from numpy import std
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.ensemble import RandomForestClassifier

training_data = []
outputs=[]
with open('POGODA/pogoda_training.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp = row[-1]
        row.pop(-1)
        outputs.append(int(temp))
        training_data.append(row)
print(len(training_data))
print(training_data[1])


with open('POGODA/pogoda_test.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp = row[-1]
        row.pop(-1)
        outputs.append(int(temp))
        training_data.append(row)
print(len(training_data))
training_data = numpy.array(training_data)
print(len(training_data[0]))
print(training_data[0])

print(len(outputs))
outputs = numpy.array(outputs)


for par_sze in [5,10,35,50,100,150,200]:

  f = open('pogoda_las_losowosci.txt', 'a')

  liczba_powtorzen = 7
  szer = par_sze

  f.writelines('--Liczba Drzew--')
  f.write('\n')
  f.writelines(str(szer))
  f.write('\n')


  lista_wynikow_lasu = []
  srednia = 0
  srednia_std = 0
  najmniejszy=1
  najwiekszy = 0

  for i in range(liczba_powtorzen):
      model = RandomForestClassifier(szer)
      cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=5, random_state=1)
      n_scores = cross_val_score(model, training_data,outputs,cv=cv)
      print('____________________')
      print(i)
      srednia+=mean(n_scores)
      srednia_std+=std(n_scores)
      if (mean(n_scores)>najwiekszy):
        najwiekszy=mean(n_scores)
      if (mean(n_scores)<najmniejszy):
        najmniejszy=mean(n_scores)
  srednia=srednia/liczba_powtorzen
  srednia_std=srednia_std/liczba_powtorzen
  

  
  

  print("______ODCHYLENIE")
  print(srednia_std)
  print("______SREDNIA")
  print(srednia)
  print("______MAKS")
  print(najwiekszy)
  print("______MINI")
  print(najmniejszy)

  f.writelines('_______LAS________')
  f.write('\n')
  f.writelines("______ODCHYLENIE")
  f.write('\n')
  f.writelines(str(srednia_std))
  f.write('\n')
  f.writelines("______SREDNIA")
  f.write('\n')
  f.writelines(str(srednia))
  f.write('\n')
  f.writelines("______MAKS")
  f.write('\n')
  f.writelines(str(najwiekszy))
  f.write('\n')
  f.writelines("______MINI")
  f.write('\n')
  f.writelines(str(najmniejszy))

  f.write('\n')
  f.writelines('')
  f.write('\n')
  f.writelines('')
  f.write('\n')

  f.close()

