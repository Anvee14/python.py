import plotly.express as px
import csv
import numpy as np


def get_data(data_path):
    i_sale = []
    drinks_sale=[]

    with open(data_path)as f:
        df = csv.DictReader(f)
        for row in df:
            i_sale.append(float(row['Temperature']))
            drinks_sale.append(float(row['Ice-cream']))
    return{'x':i_sale,
           'y' :drinks_sale}
        
def find_corel(data_src):
    corel = np.corrcoef(data_src['x'],data_src['y'])
    print('corelation between ice-cream and temp',corel[0,1])

def setup():
    data_path = 'C:/Users/anvee/my_git_projects/Python/corelation/ice-cream.csv'
    data_src = get_data(data_path)
    find_corel(data_src)
    
setup()


    
