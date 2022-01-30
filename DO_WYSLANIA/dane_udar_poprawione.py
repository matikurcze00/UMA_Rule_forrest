import csv

kompleks_ogolny = []
with open('UDAR/kompleks_ogolny_udar.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        kompleks_ogolny.append(row)
print(len(kompleks_ogolny))
print(kompleks_ogolny)


training_data = []
lista_przedzialy = [0, 1, 0, 0, 0, 0, 0, 1, 1, 0]
f = open('UDAR/udar_poprawione.csv', 'w', newline='')
writer = csv.writer(f)
with open('UDAR/healthcare-dataset-stroke-data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        row.pop(0)
        temp = row[-1]
        row.pop(-1)
        row.append(int(temp))
        if row[0] == 'Other':
            continue
        if row[8] == 'N/A':
            continue
        if row[9] == 'Unknown':
            continue
        for i, selektor in enumerate(kompleks_ogolny):
            if lista_przedzialy[i]:
                zmienna = ''
                for j, wartosc in enumerate(selektor):
                    if float(row[i]) < float(wartosc):
                        zmienna = selektor[j-1]
                        break
                    else:
                        zmienna = wartosc
                row[i] = zmienna
        training_data.append(row)
        writer.writerow(row)
f.close()
print(len(training_data))
