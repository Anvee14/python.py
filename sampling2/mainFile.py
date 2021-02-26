import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv(
    "C:/Users/anvee/my_git_projects/Python/sampling2/studentMarks.csv")
data = df["Math_score"].tolist()

# plotting the graph
fig = ff.create_distplot([data], ['Math_score'], show_hist=False)
# fig.show()
mean = statistics.mean(data)
std = statistics.stdev(data)
print(mean, std)
# code to find mean of 100 data points 1000 time


def random_setof_mean(counter):
    data_set = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        data_set.append(value)
    mean = statistics.mean(data_set)
    return mean


meanList = []
for i in range(0, 1000):
    setofmean = random_setof_mean(100)
    meanList.append(setofmean)

mean2 = statistics.mean(meanList)
std2 = statistics.stdev(meanList)

print(mean2, std2)

fig = ff.create_distplot([meanList], ['Math_score'], show_hist=False)
fig.add_trace(go.Scatter(x=[mean2, mean2], y=[
              0, 0.22], mode='lines', name='mean'))
# fig.show()
# Standard deviation of thesampling distribution = Standard deviation of thepopulation / sqrt(100).
# Standard deviation of thesampling distribution (alsocalled standard error of themean) = standard deviationof the sampling distribution /sqrt (sampling size)

# calculating 1st, 2nd and 3rd std
first_std_strt, first_std_end = mean2-std2, mean2+std2
second_std_strt, second_std_end = mean2 - \
    (2*std2), mean2+(2*std2)
third_std_strt, third_std_end = mean2 - \
    (3*std2), mean2+(3*std2)
print("STD1 ", first_std_strt, first_std_end)
print("STD2 ", second_std_strt, second_std_end)
print("STD3 ", third_std_strt, third_std_end)

# plotting the graph with traces
fig = ff.create_distplot([meanList], ["student_marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean2, mean2], y=[
              0, 0.17], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[first_std_strt, first_std_strt], y=[
              0, 0.17], mode="lines", name="std 1 start"))
fig.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[
              0, 0.17], mode="lines", name="std 1 end"))
fig.add_trace(go.Scatter(x=[second_std_strt, second_std_strt], y=[
              0, 0.17], mode="lines", name="std 2 start"))
fig.add_trace(go.Scatter(x=[second_std_end, second_std_end], y=[
              0, 0.17], mode="lines", name="std 2 end"))
fig.add_trace(go.Scatter(x=[third_std_strt, third_std_strt], y=[
              0, 0.17], mode="lines", name="std 3 start"))
fig.add_trace(go.Scatter(x=[third_std_end, third_std_end], y=[
              0, 0.17], mode="lines", name="std 3 end"))
fig.show()
