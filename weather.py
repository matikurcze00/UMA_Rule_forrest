import csv
with open('weather_kompleks.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    header =next(reader)
print(header)
data = []
with open('weatherAUS_noNADataOutput.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
      if(row[0] in header):
        temp = []
        temp.append(row[0])
        temp.append(int(float(row[1])-(float(row[1])%5)))
        temp.append(int(float(row[2])-(float(row[2])%5)))
        temp.append(int(float(row[3])-(float(row[3])%10)))
        temp.append(int(float(row[4])-(float(row[4])%5)))
        temp.append(int(float(row[5])-(float(row[5])%5)))
        temp.append(int(float(row[7])-(float(row[7])%20)))
        temp.append(int(float(row[10])-(float(row[10])%20)))
        temp.append(int(float(row[11])-(float(row[11])%20)))
        temp.append(int(float(row[12])-(float(row[12])%20)))
        temp.append(int(float(row[13])-(float(row[13])%20)))
        temp.append(int(float(row[14])-(float(row[14])%20)))
        temp.append(int(float(row[15])-(float(row[15])%20)))
        temp.append(int(float(row[16])-(float(row[16])%2)))
        temp.append(int(float(row[17])-(float(row[17])%2)))
        temp.append(int(float(row[18])-(float(row[18])%5)))
        temp.append(int(float(row[19])-(float(row[19])%5)))
        temp.append(row[20])
        temp.append(row[21])
        data.append(temp)

with open('weather.csv','w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  for row in data:
    writer.writerow(row)
