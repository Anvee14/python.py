from collections import Counter
import csv
with open('C:/Users/anvee/my_git_projects/Python/Data_visualization/Mean,median,mode/height-weight.csv', newline='')as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []
for i in range(len(file_data)):
    num = file_data[i][1]
    new_data.append(num)

data = Counter(new_data)
mode_data_for_range = {
    "50-60":0,
    "60-70":0,
    "70-80":0
}
for height,occourance in data.items():
    if 50 < float(height)<60:
        mode_data_for_range["50-60"]+= occourance
    elif 60 < float(height)<70:
        mode_data_for_range["60-70"]+= occourance
    elif 70 < float(height)<80:
        mode_data_for_range["70-80"]+= occourance

mode_range,mode_occourance = 0,0
for range,occourance in mode_data_for_range.items():
    if occourance > mode_occourance:
        mode_range, mode_occourance = [
            int(range.split('-')[0]), int(range.split('-')[1])],occourance
        

print(mode_range,mode_occourance)
print(mode_occourance)
mode = float((mode_range[0]+mode_range[1]/2))
print(mode)
print(data)
