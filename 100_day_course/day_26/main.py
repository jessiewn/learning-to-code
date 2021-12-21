student_dict={"students":["Angela","lily","score"],"score":[56,76,98]}
# for (key,value) in student_dict.items():
#     print(key)


import pandas
student_data_frame=pandas.DataFrame(student_dict)
print(student_data_frame)

# for (key,value) in student_data_frame.items():
#     print(value)

for (index,row) in student_data_frame.iterrows():
    print(index)

{new_key:new_value for (index,row) in df.interrows()}


#TODO1, create a dictionary in this format:
{"A":"Alfa",}

#create a list of the phonetic code words