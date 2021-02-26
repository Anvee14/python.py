import numpy as np
import csv
import plotly.express as px


def get_data(data_path):
    coffee = []
    sleep = []

    with open(data_path)as f:
        df = csv.DictReader(f)
        for row in df:
            coffee.append(float(row['Coffee']))
            sleep.append(float(row['Sleep']))
    return{'x': coffee,
           'y': sleep}


def find_corel(data_src):
    corel = np.corrcoef(data_src['x'], data_src['y'])
    print('corelation between coffee and sleep', corel[0, 1])


def setup():
    data_path = 'C:/Users/anvee/my_git_projects/Python/corelation/coffee_sleep.csv'
    data_src = get_data(data_path)
    find_corel(data_src)


setup()
