student_heights=input('intput some numbers?') 


split_student_height= student_heights.split()
print(student_heights)
print(split_student_height)

sum=0
n=0
for str1 in split_student_height:
    after_float=float(str1)
    print(after_float)
    print (type(after_float))
    after_round=round(after_float)
    print(after_round)
    sum=sum+after_round
    print(f'sum is {sum}')
    n=n+1

height_average=round(sum/n)
print(f'average height is {height_average}')