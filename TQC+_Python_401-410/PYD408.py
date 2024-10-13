a = []
even = 0
odd = 0

for i in range(10):
    a.append(eval(input()))

    if a[-1] % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even numbers: %d" %(even))
print("Odd numbers: %d" %(odd))

