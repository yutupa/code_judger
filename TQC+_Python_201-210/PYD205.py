i = input()

if i.isalpha():
    print(i, "is an alphabet.")
elif i.isnumeric():
    print(i, "is a number.")
else:
    print(i, "is a symbol.")