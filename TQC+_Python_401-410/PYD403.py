a = eval(input())
b = eval(input())

count = 0
sum = 0
for i in range(a, b+1):
    if (i%4 == 0) or (i%9 == 0):
        count = count + 1
        sum = sum + i
        print("%-4d" %(i), end = "")
        if count%10 == 0:
            print("")

print("")
print(count)
print(sum)