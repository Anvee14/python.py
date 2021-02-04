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
    print(num)
    new_data.append(float(num))

n = len(new_data)
total = 0
for x in new_data:
    total+=x
mean = total/n
print('mean is '+str(mean))
    


