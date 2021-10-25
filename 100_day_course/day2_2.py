a = 4/3
b = 69.34356

# print(a)
# print(type(a))

#message = "the value of a is " + str(a)
#print(message)

# message = "the value of a is {}"
# print("- Message without format is ")
# print(message)

template= "the value of a is {:15.2f} but value of b is {:.1f}"
message = template.format(a, b)
print("- Message with format is ")
print(message)
