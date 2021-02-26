import plotly.figure_factory as ff
import statistics 
import random
import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv("C:/Users/anvee/my_git_projects/Python/sampling/newdata.csv")
data = df["average"].tolist()
mean = statistics.mean(data)
std = statistics.stdev(data)
figure = ff.create_distplot([data],["average"],show_hist=False)
figure.add_trace(go.Scatter(x = [mean,mean], y = [0,2],mode = 'lines', name = 'mean'))
#figure.show()
#print(mean,std)
#code to find mean and std of 100 data points
data_set = []
for i in range(0,1000):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    data_set.append(value)

mean1 = statistics.mean(data_set)
std1 = statistics.stdev(data_set)
print(mean,mean1,'\n',std,std1)
figure = ff.create_distplot([data_set], ["average"], show_hist=False)
figure.add_trace(go.Scatter(x=[std1], y=[
                 0, 2], mode='lines', name='mean'))
figure.show()
