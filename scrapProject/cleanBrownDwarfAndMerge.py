import pandas as pd
df = pd.read_csv('C:/Users/anvee/my_git_projects/Python/scrapProject/brown_dwarf.csv')
df.columns
print(df)
df.dtypes
df = df.dropna()
df.dtypes
#df.drop()
df["Radius"] = 0.102763*df["Radius"]
#df['Mass']=df['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
# Sorting planet names in alphabetical order
df["Mass"] = 0.000954588*df["Mass"]
df.dtypes
df.head()
df.columns
df.drop(['Unnamed: 0'],axis=1,inplace=True)
df.head()
df.reset_index(drop=True,inplace=True)
df.to_csv("unit_converted_stars.csv")
import csv
import pandas as pd

file1 = 'bright_stars.csv'
file2 = 'unit_converted_stars.csv'

d1 = []
d2 = []

with open(file1,'r') as f:
    csv_reader =csv.reader(f)
    
    for i in csv_reader:
        d1.append(i)
        
with open(file2,'r') as f:
    csv_reader = csv.reader(f)
    
    for i in csv_reader:
        d2.append(i)


h1 = d1[0]
h2 = d2[0]
header=h1+h2