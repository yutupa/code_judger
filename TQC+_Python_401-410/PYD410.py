n = eval(input())

for i in range(n):
    for j in range(n - i - 1):
        print(' ', end="")
    for j in range((2 * i + 1)):
        print('*', end="")

    print()
    

'''
for i in range(n):
    for j in range((2*n-1)):
        if j < (n - 1):
            if (n - i - j -2) >= 0:
                print(' ', end="")
            else:
                print('*', end="")
        elif j == (n - 1):
            print('*', end="")
        else:
            if (n + i - j - 1) < 0:
                print('', end="")
            else:
                print('*', end="")
    print()
'''
