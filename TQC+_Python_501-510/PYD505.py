def compute(a, x, y):
    for i in range(y):
        for j in range(x):
            print(a, " ", end = "")
        print()

char = input()
m = eval(input())
n = eval(input())

compute(char, m, n)
        