import pandas as pd
import csv
import plotly.figure_factory as ff
df = pd.read_csv("C:/Users/anvee/my_git_projects/Python/bellCurve/data.csv")
figure = ff.create_distplot([df["Weight(Pounds)"].tolist()], [
                            "weight"], show_hist=True)
figure.show()
