# with open("weather_data.csv") as data:
#     data = data.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)  # This created an object loop through too print every row as list
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
# print(type(data))  # type would be a data frame: means the complete table is considered as a data frame
# print(type(data["temp"]))  # type would be series : means a column in the table is considered as series object

# data_dict = data.to_dict()
# print(data_dict)

# data_list = data["temp"].to_list()
# print(data_list)

# My way:
# t_num = 0
# for num in data_list:
#     t_num += num
#
# average = t_num/len(data_list)
# print(average)

# Her way:
# average = sum(data_list)/len(data_list)
# print(average)

# other way
# print(data["temp"].mean())

# Get Data in Columns
# print(data["condition"])  # treating data as dict. calling by key
# print(data.condition)  # treating as object calling by attribute

# Get data in row
# print(data[data.day == "Monday"])
# data_max = data["temp"].max()
# print(data[data.temp == data_max])

# using row to access values of other columns
# monday = data[data.day == "Monday"]
# print(monday.condition)
# temp = int(monday.temp)
# fahrenheit = temp * 1.8 + 32
# print(fahrenheit)

# create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "John", "Angela"],
#     "scores": [76, 56, 65]
# }
# data_dic = pandas.DataFrame(data_dict)
# print(data_dic)
# data_dic.to_csv("dict_data.csv")

data = pandas.read_csv("228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
grey_squirrel = data[data["Primary Fur Color"] == "Gray"]
red_squirrel = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrel = data[data["Primary Fur Color"] == "Black"]
grey_count = len(grey_squirrel)
red_count = len(red_squirrel)
black_count = len(black_squirrel)
print(grey_count)
print(red_count)
print(black_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "count": [grey_count, red_count, black_count]
}

data_dic = pandas.DataFrame(data_dict)
data_dic.to_csv("squirrel_count.csv")
