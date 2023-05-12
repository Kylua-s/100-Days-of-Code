# Exercise 37 - Squirrels
# Count the amount squirrels by their fur color

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_fur = data["Primary Fur Color"].value_counts()
squirrel_fur.to_csv("squirrel_amount_by_fur.csv")
