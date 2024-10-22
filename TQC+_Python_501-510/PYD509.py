import math

def compute(p, q):
    return math.gcd(p, q)

x, y = eval(input())
m, n = eval(input())

q = y * n
p = m * y + x * n
gcd = compute(p, q)

print('%d/%d + %d/%d = %d/%d' %(x, y, m, n, int(p/gcd), int(q/gcd)))