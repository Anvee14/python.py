import pandas as pd
import csv
import plotly.graph_objects as go
df = pd.read_csv('C:/Users/anvee/my_git_projects/Python/pixcel_math/data.csv')
# print(df.groupby('level')['student_id'].mean())
student_ID = df.loc[df['student_id'] == 'TRL_987']
fig = go.Figure(go.Bar(
    x=student_ID.groupby('level')['attempt'].mean(),
    y=['Level 1', 'Level 2', 'Level 3', 'Level 4'],
    orientation='h',
))
fig.show()
