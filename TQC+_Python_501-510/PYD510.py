def compute(num):
    F = [0, 1]
    for n in range(2, num):
        F.append(F[n - 1] + F[n - 2])
        
    for i in F:
        print(i, end=' ')
    print()

num = eval(input())
compute(num)