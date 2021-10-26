#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# def choice(values):
#     random_number= random.randint(0,len(values))
#     a=random_number

##################

#pick_number=random.randint(0,len(letters))
# print(pick_number)
# print(letters[pick_number])

# pick_number_number=random.randint(0,len(numbers))
# print(numbers[pick_number_number])

# pick_number_symbol=random.randint(0,len(symbols))
# print(symbols[pick_number_symbol])

########################

def print_choice(values):
    pick_number_symbol=random.randint(0,len(values))
    print(values[pick_number_symbol])



# print_choice(numbers)
# print_choice(symbols)
# print_choice(letters)
###############################
def choice(values):
    pick_number_symbol=random.randint(0,len(values)-1)
    value = values[pick_number_symbol]
    return  value

x = choice(numbers)
print(x)

x = choice(symbols)
print(x)

x = choice(letters)
print(x)

# print("Welcome to the PyPassword Generator!")


nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

list_letters=[]
list_numbers=[]
list_symbols=[]

for n in range(0,nr_letters):
   x=choice(letters)
   list_letters.append(x)
   print(choice(numbers))
   y=choice(numbers)
   list_numbers.append(y)
   z=choice(symbols)
   list_symbols.append(z)
psw_list=[list_letters,list_numbers,list_symbols]
print(psw_list)
str1=''.join(list_letters)
str2=''.join(list_numbers)
str3=''.join(list_symbols)
print(str1+str2+str3)

    

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P