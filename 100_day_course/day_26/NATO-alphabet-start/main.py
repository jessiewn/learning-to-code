student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data=pandas.read_csv("100_day_course/day_26/NATO-alphabet-start/nato_phonetic_alphabet.csv")
#nato={}
# for (index,row) in data.iterrows():
#     nato[f"{row.letter}"]=row.code
nato={row.letter:row.code for (index,row) in data.iterrows()}
print(nato)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# word=list(input("what is your words?\n").upper())
# new_list=[]
# for letter in word:
    
#     print(letter)
#     new_dic=[row.code for (row.letter,row.code) in nato.items() if letter==row.letter]
# new_list.extend(new_dic)

# print(new_list)
word=input("Enter your word").upper()
output_list=[nato[letter] for letter in word]
print(output_list)

#result = [int(num) for num in list1 if num in list2]
