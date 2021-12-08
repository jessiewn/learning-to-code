with open("/Users/nan/coding/learning-to-code/100_day_course/day_24/my_file.txt",mode="a") as file:

    file.write("\nNew text")

with open("new_file.txt",mode="w") as file:
    file.write("new file")