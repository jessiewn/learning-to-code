#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print('Welcome to tip caculator')
# total_bill=input('what was your total bill?')
# tip_per= input('what percentage tip you would like to give?10,12, or 15?')
# number_people=input('how many people want to split the bill?')


total_bill='124.56'
tip_per='12'
number_people='7'

tip_per_int= int(tip_per)
print(type(tip_per_int))
tip_in_per=tip_per_int/100
total_bill_f= float(total_bill)
number_people_f=float(number_people)
tip_in_per_f=float(tip_in_per)
each_pay=total_bill_f*(1+tip_in_per_f)/number_people_f
each_pay_r=round(each_pay,2)
print(f'each one should pay{each_pay_r}')