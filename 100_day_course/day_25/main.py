

import csv
import pandas
import statistics




# with open("/Users/nan/coding/learning-to-code/100_day_course/day_25/weather_data.csv") as file:
#     data=csv.reader(file)
#     temperetures=[]
#     for row in data:
#         if row[1]!="temp":
#             tem=int(row[1])
#             temperetures.append(tem)
#     print(temperetures)



#data=pandas.read_csv("/Users/nan/coding/learning-to-code/100_day_course/day_25/weather_data.csv")
# print(data)

# print(data["temp"])

# temp_list=data["temp"].to_list()
# print(temp_list)

# print(statistics.mean(temp_list))
# print(data["temp"].max())
#print(data[data.day=="Monday"])
#print(data[data.temp==data.temp.max()])
# monday= data[data.day=="Monday"]
# print(monday.condition)
# print((int(monday.temp)*1.8)+32)

data=pandas.read_csv("/Users/nan/coding/learning-to-code/100_day_course/day_25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


fur_gray=data[data["Primary Fur Color"]=="Gray"]
gray_list=fur_gray["Primary Fur Color"].to_list()
len(gray_list)
fur_red=data[data["Primary Fur Color"]=="Cinnamon"]
red_list=fur_red["Primary Fur Color"].to_list()
len(red_list)
fur_black=data[data["Primary Fur Color"]=="Black"]
black_list=fur_gray["Primary Fur Color"].to_list()
len(black_list)


#df = pd.DataFrame({'name': ['Raphael', 'Donatello'],'mask': ['red', 'purple'],'weapon': ['sai', 'bo staff']})
#df.to_csv(index=False)
pre_csv=pandas.DataFrame({"Fur Color":["grey","red","black"],"Count":[f"{len(gray_list)}",f"{len(red_list)}",f"{len(black_list)}"]})
pre_csv.to_csv("/Users/nan/coding/learning-to-code/100_day_course/day_25/squirrel_count.csv")