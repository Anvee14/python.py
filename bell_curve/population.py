import pandas as pd
import statistics
import csv

df = pd.read_csv("C:/Users/anvee/my_git_projects/Python/bellCurve/data.csv")
height_list = df["Height(Inches)"].to_list()
weight_list = df["Weight(Pounds)"].to_list()
# mean for height and weight
height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)

# median for height and weight
height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)

# mode for height and weight
height_mode = statistics.mode(height_list)
weight_mode = statistics.mode(weight_list)


print("mean,median and mode is {},{} and {} ".format(
    height_mean, height_median, height_mode))
print("mean,median and mode is {},{} and {} ".format(
    weight_mean, weight_median, weight_mode))
# standard deviation
height_std = statistics.stdev(height_list)
weight_std = statistics.stdev(weight_list)
# 1,2,3 for height
h_1std_start, h_1std_end = height_mean - height_std, height_mean+height_std

h_2std_start, h_2std_end = height_mean - \
    (2*height_std), height_mean+(2*height_std)

h_3std_start, h_3std_end = height_mean - \
    (3*height_std), height_mean+(3*height_std)
# 1,2,3 for weight
w_1std_start, w_1std_end = weight_mean - weight_std, weight_mean+weight_std

w_2std_start, w_2std_end = weight_mean - \
    (2*weight_std), weight_mean+(2*weight_std)

w_3std_start, w_3std_end = weight_mean - \
    (3*weight_std), weight_mean+(3*weight_std)

# percentage of data lie within 1,2 and 3rd std  for height
h_of_data_within_1ststd = [
    result for result in height_list if result > h_1std_start and result < h_1std_end]
h_of_data_within_2ststd = [
    result for result in height_list if result > h_2std_start and result < h_2std_end]
h_of_data_within_3ststd = [
    result for result in height_list if result > h_3std_start and result < h_3std_end]

# percentage of data lie within 1,2 and 3rd std  for weight
w_of_data_within_1ststd = [
    result for result in weight_list if result > w_1std_start and result < w_1std_end]
w_of_data_within_2ststd = [
    result for result in weight_list if result > w_2std_start and result < w_2std_end]
w_of_data_within_3ststd = [
    result for result in weight_list if result > w_3std_start and result < w_3std_end]

# height
print("{} % of data for height lies within 1st std deviation".format(
    len(h_of_data_within_1ststd)*100.0/len(height_list)))
print("{} % of data for height lies within 2st std deviation".format(
    len(h_of_data_within_2ststd)*100.0/len(height_list)))
print("{} % of data for height lies within 3st std deviation".format(
    len(h_of_data_within_3ststd)*100.0/len(height_list)))

# weight
print("{} % of data for weight lies within 1st std deviation".format(
    len(w_of_data_within_1ststd)*100.0/len(weight_list)))
print("{} % of data for weight lies within 2st std deviation".format(
    len(w_of_data_within_2ststd)*100.0/len(weight_list)))
print("{} % of data for weight lies within 3st std deviation".format(
    len(w_of_data_within_3ststd)*100.0/len(weight_list)))
