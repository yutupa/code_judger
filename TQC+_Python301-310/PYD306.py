n = eval(input())

factorial = 1

for i in range(1, n+1):
    factorial *= i

print(factorial)

''' Another method
import math
n = eval(input())
print(math.factorial(n))
'''