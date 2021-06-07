import csv
data1 = []
data2 = []
with open("dataSet1.csv", "r")as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        data1.append(row)

with open("dataset_2_sorted.csv", "r")as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        data2.append(row)

headers1 = data1[0]
planet_data1 = data1[1:]
headers2 = data2[0]
planet_data2 = data2[1:]
headers = headers1+headers2
planetdata = []
for index,data_row in enumerate(planet_data1):
    planetdata.append(planet_data1[index]+planet_data2[index])

with open("merged.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdata)
    
