import random
import plotly.express as px
import plotly.figure_factory as ff
import statistics
dice_result = []
count = []
for i in range(0,100000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1, 6)
    dice_result.append(dice1+dice2)
    count.append(i)
mean = statistics.mean(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)
print(mean," ,",mode,",",median)
figure = ff.create_distplot([dice_result], ["result"], show_hist=False)
figure.show()
