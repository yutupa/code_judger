import math

n = eval(input())

answer = 0

for i in range(1, n):
    answer = answer + 1 / (math.sqrt(i) + math.sqrt(i+1))

print('%.4f' % answer)