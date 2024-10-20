def compute(a, b):
    s = 0
    for i in range(a, b+1):
        s = s + i
    return s

x = eval(input())
y = eval(input())

print(compute(x, y))