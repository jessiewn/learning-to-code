f = open("/Users/nan/coding/learning-to-code/100_day_course/day_24/Mail Merge Project Start/Input/Names/invited_names.txt", "r")
txt=f.readlines()
print(txt)




for name in txt:
    x = name.strip("\n")

    print(x)

txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)