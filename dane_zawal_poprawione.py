import csv


kompleks_ogolny = []
with open('ZAWAL/kompleks_ogolny_zawal.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        kompleks_ogolny.append(row)


training_data = []
lista_przedzialy = [1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0]
f = open('ZAWAL/zawal_poprawione.csv', 'w', newline='')
writer = csv.writer(f)
with open('ZAWAL/heart.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp = row[-1]
        row.pop(-1)
        row.append(int(temp))
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
