#1
cars = ["Audi", "Infinity", "Lada", "Mercedes", "Mitsubishi", "KIA"]
prices = [10000, 15000, 20000, 25000, 30000, 35000]
he = dict(zip(cars, prices))
print(he)

#2
import csv

with open ("cars.csv", "w", encoding= "utf-8") as f:
    writer = csv.writer(f, delimiter=";", lineterminator="\r")
    writer.writerow(["cars", "prices"])
    for x in range(5):
        row = [cars[x], prices[x]]
        writer.writerow(row)
#3
with open(r"c:\Users\User\Desktop\list.txt") as d:
    text = d.read()
    letters = text.count("D")
    print(letters)
