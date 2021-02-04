import pandas as pd
import plotly.express as px

df = pd.read_csv("C:/Users/anvee/my_git_projects/Python/Data_visualization/practice/data.csv")
print(df)
figure = px.pie(df, title='Internet users')
figure.show()
