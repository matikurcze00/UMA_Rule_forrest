import csv
import random

data =[]
with open('weatherAUS_noNADataOutput.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
      if(row[0] == 'Sydney'):
        temp = []
        temp.append(int(float(row[3])-(float(row[3])%30)))
        temp.append(int(float(row[4])-(float(row[4])%10)))
        temp.append(int(float(row[5])-(float(row[5])%5)))
        temp.append(int(float(row[7])-(float(row[7])%25)))
        temp.append(int(float(row[11])-(float(row[11])%25)))
        temp.append(int(float(row[13])-(float(row[13])%25)))
        temp.append(int(float(row[15])-(float(row[15])%25)))
        temp.append(int(float(row[17])-(float(row[17])%3)))
        temp.append(int(float(row[19])-(float(row[19])%15)))
        temp.append(row[20])
        temp.append(row[21])
        data.append(temp)

random.shuffle(data)

with open('POGODA/pogoda.csv','w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  for row in data:
    writer.writerow(row)
