import pandas as pd
import plotly.express as px
'''data = [00,11,22,33,44,55,66]
df = pd.DataFrame(data)
print(df)'''
df = pd.read_csv("C:/Users/anvee/my_git_projects/Python/Data_visualization/data.csv")
figure = px.parallel_coordinates(df, title='Internet users')
figure.show()
