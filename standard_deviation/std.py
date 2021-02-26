import math
import csv
with open('C:/Users/anvee/my_git_projects/Python/standard_deviation/data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
data = file_data[0]
#finding mean
def mean(data):
    n = len(data)
    total = 0
    for x in data :
        total+=int(x)

    mean = total/n
    return mean 

#getting values
square_list = []
for num in data :
    a = int(num)-mean(data)
    a = a**2
    square_list.append(a)

print(square_list)
#getting sum
sum = 0
for i in square_list:
    sum = sum+i

#dividing the sum by total
result = sum/(len(data)-1)
std = math.sqrt(result)
print(std)
