student_heights=input('intput some numbers?') 


split_student_height= student_heights.split()
print(student_heights)
print(split_student_height)

sum=0
for str1 in split_student_height:
    after_float=float(str1)
    print(after_float)
    print (type(after_float))
    after_round=round(after_float)
    print(after_round)
    sum=sum+after_round
    print(f'sum is {sum}')
n= len(split_student_height)
print(n)
height_average=round(sum/n)
print(height_average)