n = eval(input())
t = 1+2*(n-1)

for i in range(n):
    for j in range(t):
        if (j-i) > t/2:
            print(' ', end="")
        else:
            print('*', end="")
    print()

