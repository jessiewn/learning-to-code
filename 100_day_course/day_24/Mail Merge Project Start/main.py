#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

from pathlib import Path

file_path = Path(__file__).resolve()
file_parent = file_path.parent
my_file = file_parent / "Input/Letters/starting_letter.txt"

f = open("/Users/nan/coding/learning-to-code/100_day_course/day_24/Mail Merge Project Start/Input/Names/invited_names.txt", "r")
names=f.readlines()
names_list=[]

for name in names:
    x = name.strip("\n")
    names_list.append(x)
print(names_list)

with my_file.open(mode="r") as file:
    letter=file.read()

for name in names_list:
    x=letter.replace("[name]",name)
    with open(f"/Users/nan/coding/learning-to-code/100_day_course/day_24/Mail Merge Project Start/Output/ReadyToSend/{name}_letter.txt",mode="w")as file:
        file.write(x)

        
    






