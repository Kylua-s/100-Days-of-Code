# Exercise 36 - Pandas CSV
# Different task to learn working with the pandas library

import pandas

data = pandas.read_csv("weather_data.csv")


# Data in a column
print("Temp column: ")
print(data.temp)
print()


# Get Data in Row
print("Data from Monday:")
print(data[data.day == "Monday"])
print()


# Converts the table to a dictionary
print("Table to Dictionary:")
data_dict = data.to_dict()
print(data_dict)
print()


# Average and max data
print("Average temperature:")
print(data.temp.mean())
print("Max temperature:")
print(data.temp.max())
print()


# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("student_score.csv")
