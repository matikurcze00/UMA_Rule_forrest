import csv
kompleks=[]
for i in range(19):
  kompleks.append([])
with open('weather.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    for row in reader:
      for i in range(19):
        if (row[i] not in kompleks[i]):
          kompleks[i].append(row[i])
for kom in kompleks:
  print(kom)