import csv
kompleks=[]
for i in range(14):
  kompleks.append([])
with open('POGODA/pogoda.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    for row in reader:
      for i in range(11):
        if (row[i] not in kompleks[i]):
          kompleks[i].append(row[i])
for kom in kompleks:
  print(kom)