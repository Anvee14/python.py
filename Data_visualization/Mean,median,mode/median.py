import csv
from collections import Counter
with open('C:/Users/anvee/my_git_projects/Python/Data_visualization/Mean,median,mode/height-weight.csv', newline='')as f:
    reader = csv.reader(f)
    file_data = list(reader)
    #print(file_data[0])

file_data.pop(0)
#shorting data to get the height of people
new_data = []
for i in range(len(file_data)):
    num = file_data[i][1]
    new_data.append(float(num))

n = len(new_data)
new_data.sort()
if n % 2 == 0:
    median1 = float(new_data[n//2])
    median2 = float(new_data[n//2-1])
    median = (median1+median2)/2
    print(median1,median2)

else :
    median = new_data[n//2]

print('median is :' + str(median))
     

