
#add
def add(n1,n2):
  return n1+n2
#substract
def substract(n1,n2):
  return n1-n2

#multiply
def multiply(n1,n2):
  return n1*n2

#divide
def divide(n1,n2):
  return n1/n2

operations={}
operations['+']=add
operations['-']=substract
operations['*']=multiply
operations['/']=divide

num1=int(input('what is the first number?\n'))
num2=int(input('what is the second number?\n'))

for key in operations:
  print(key)
operaton_symbol=input('pick one of above symbols: ')
function_name=operations[operaton_symbol]
answer=function_name(num1,num2)


print(f'{num1}{operaton_symbol}{num2}={answer}')