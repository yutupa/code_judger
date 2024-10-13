a = eval(input())

while True:
    if (a // 10) == 0:
        print(a)
        break
    print(a%10, end="")
    a = a // 10