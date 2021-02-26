# giving ipad tablets with learning materials in it
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv(
    'C:/Users/anvee/my_git_projects/Python/sampling2/studentMarks.csv')
data = df['Math_score'].tolist()


def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0, 1000):
    set_of_mean = random_set_of_mean(100)
    mean_list.append(set_of_mean)

mean = statistics.mean(mean_list)
std_deviation = statistics.stdev(mean_list)
first_std_strt, first_std_end = mean-std_deviation, mean+std_deviation


df = pd.read_csv(
    'C:/Users/anvee/my_git_projects/Python/sampling2/data1.csv')
data1 = df['Math_score'].tolist()
mean_of_sample1 = statistics.mean(data1)
print("Mean of sample1 ", mean_of_sample1)
fig = ff.create_distplot([mean_list], ["student_marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[
              0, 0.20], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[
              0, 0.17], mode="lines", name="mean of sample 1"))
fig.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[
              0, 0.17], mode="lines", name="std 1 end"))
fig.show()


# finding the z score using teh formula
z_score = (mean_of_sample1-mean)/std_deviation
print("the z_score is= ", z_score)
