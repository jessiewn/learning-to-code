def if_only(x):
    if x > 12:
        print("if_only: A")
    if x < 30:
        print("if_only: B")

def if_elif(x):
    if x > 12:
        print("if_elif: A")
    elif x < 30:
        print("if_elif: B")

if_only(15)
if_elif(15)

# if_only: A
# if_only: B
# if_elif: A
