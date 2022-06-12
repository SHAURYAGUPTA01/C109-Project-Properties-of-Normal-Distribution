import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd 

df = pd.read_csv("StudentsPerformance.csv")
reading  = df["reading score"].tolist()

mean = statistics.mean(reading)
std = statistics.stdev(reading)
median = statistics.median(reading)
mode = statistics.mode(reading)

print("Mean of data is  : {}".format(mean)) 
print("Median of data is : {} ".format(median))
print("Mode of data is : {} ".format(mode))

first_std_start , first_std_end = mean-std , mean+std

second_std_start , second_std_end = mean - (2*std) , mean + (2*std)

third_std_start , third_std_end = mean - (3*std) , mean + (3*std)

fig = ff.create_distplot( [reading] , ["result"])

fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN" ))

fig.add_trace(go.Scatter(x = [first_std_start,first_std_start] , y = [0 , 0.17] , mode = "lines", name = "First STD Start"))

fig.add_trace(go.Scatter(x = [first_std_end,first_std_end] , y = [0 , 0.17] , mode = "lines", name = "First STD end"))

fig.add_trace(go.Scatter(x = [second_std_start,second_std_start] , y = [0 , 0.17] , mode = "lines", name = "Second STD Start"))

fig.add_trace(go.Scatter(x = [second_std_end,second_std_end] , y = [0 , 0.17] , mode = "lines", name = "Second STD end"))

fig.add_trace(go.Scatter(x = [third_std_start,third_std_start] , y = [0 , 0.17] , mode = "lines", name = "Third STD Start"))

fig.add_trace(go.Scatter(x = [third_std_end,third_std_end] , y = [0 , 0.17] , mode = "lines", name = "Third STD end"))

fig.show()

data_std1 = [result for result in reading if result > first_std_start and result < first_std_end]

data_std2 = [result for result in reading if result > second_std_start and result < second_std_end]

data_std3 = [result for result in reading if result > third_std_start and result < third_std_end]

print("{} % of data within 1st standard deviation".format(len(data_std1) * 100 / len(reading)))
print("{} % of data within 2nd standard deviation".format(len(data_std2) * 100 / len(reading)))
print("{} % of data within 3rd standard deviation".format(len(data_std3) * 100 / len(reading)))