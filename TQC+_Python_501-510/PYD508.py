import math

def compute(x, y):
    for i in range(min(x, y), 1, -1):
        if (y%i == 0) and (x%i == 0):
            return i

x, y = eval(input())
print(compute(x, y))

'''
def compute(x,y):
    while(y!=0):
      temp=y
      y=x%y
      x=temp
    print(x)
x,y=eval(input())
compute(x,y)
'''