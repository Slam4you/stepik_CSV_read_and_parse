# Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе
# Чикаго с 2001 года по настоящее время.
#
# Одним из атрибутов преступления является его тип – Primary Type.
#
# Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.
import csv


crimedict = {}
with open("Crimes.csv", "r") as f:
    reader = csv.reader(f)
    for line in reader:
        print(line)
        print(line[5])
        if line[5] not in crimedict:
            crimedict[line[5]] = 1
        else:
            crimedict[line[5]] += 1

print(crimedict)
print(max(crimedict, key=crimedict.get))  # макс значение по value словаря
