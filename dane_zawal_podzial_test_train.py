import csv
import random

training_data_2 = []
with open('ZAWAL/zawal_poprawione.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp = row[-1]
        row.pop(-1)
        row.append(int(temp))
        training_data_2.append(row)
print(len(training_data_2))

random.shuffle(training_data_2)

train_data = []
test_data = []
for i, data in enumerate(training_data_2):
    if i % 10 == 3 or i % 10 == 6 or i % 10 == 0:
        test_data.append(data)
    else:
        train_data.append(data)

print(len(test_data))
print(len(train_data))


f = open('ZAWAL/zawal_test.csv', 'w', newline='')
writer = csv.writer(f)
for data in test_data:
    writer.writerow(data)
f.close()

f = open('ZAWAL/zawal_training.csv', 'w', newline='')
writer = csv.writer(f)
for data in train_data:
    writer.writerow(data)
f.close()


# # Dane unikalne w przykladach
# lista = [[], [], [], [], [], [], [], [], [], [], [], [], []]
# for data in train_data:
#     for i, selektor in enumerate(data):
#         if i == 14:
#             break
#         if selektor not in lista[i]:
#             lista[i].append(selektor)

# for data in test_data:
#     for i, selektor in enumerate(data):
#         if i == 14:
#             break
#         if selektor not in lista[i]:
#             lista[i].append(selektor)

# for lis in lista:
#     lis.sort()
# print(lista)
