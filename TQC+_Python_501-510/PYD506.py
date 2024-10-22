import math

def compute(a, b, c):
    if math.pow(b, 2) - 4 * a * c >= 0:
        ans1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        ans2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        return ans1, ans2
    else:
        print('Your equation has no root.')
        return None, None

a = eval(input())
b = eval(input())
c = eval(input())

ans1, ans2 = compute(a, b, c)

if ans1 != None:
    if ans1 == ans2:
        print("%.1f" %(ans1))
    else:
        print("%.1f, %.1f" %(ans1, ans2))
