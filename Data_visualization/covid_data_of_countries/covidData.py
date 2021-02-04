import pandas as pd
import plotly.express as px
df = pd.read_csv(
    "C:/Users/anvee/my_git_projects/Python/Data_visualization/covid_data_of_countries/covidData.csv")
figure = px.scatter(df, x='date', y='cases', color='country' , title='Covid cases in various countries')
figure.show()
