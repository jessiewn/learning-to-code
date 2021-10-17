# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_int = int(age)
age_left = 90 - age_int
#print(age_left)
month_left= 12* age_left
weeks_left= 52* age_left
days_left=365* age_left
print(f'you have {days_left} days,{weeks_left} weeks, {month_left} months left' )