import plotly.express as px
import csv
import numpy as np


def get_data(data_path):
    marks = []
    days_present=[]

    with open(data_path)as f:
        df = csv.DictReader(f)
        for row in df:
            marks.append(float(row['Marks In Percentage']))
            days_present.append(float(row['Days Present']))
    return{'x':marks,
           'y' :days_present}

       
def find_corel(data_src):
    corel = np.corrcoef(data_src['x'],data_src['y'])
    print('corelation between marks and absence',corel[0,1])
    print(corel)

def setup():
    data_path = 'C:/Users/anvee/my_git_projects/Python/corelation/StudentMarks_DaysPresent.csv'
    data_src = get_data(data_path)
    find_corel(data_src)
    
setup()


    
