import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv("C:/Users/anvee/my_git_projects/Python/sampling/newdata.csv")
data = df["average"].tolist()


def random_setof_mean(counter):
    data_set = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        data_set.append(value)
    mean  = statistics.mean(data_set)
    return mean

def show_figure(mean_list):
    df = mean_list
    fig = ff.create_distplot([df],["average"],show_hist = False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,500):
        setof_mean = random_setof_mean(250)
        mean_list.append(setof_mean)
    show_figure(mean_list)
setup()