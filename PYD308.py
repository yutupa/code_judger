'''
for i in range(int(input())):
    n=str(input())
    a = [int(j) for j in list(str(n))] # 將對應的數字轉換成數字串列，例如 11 轉換成 [1, 1]
    print("Sum of all digits of "+str(n)+" is "+str(sum(a)))
'''

n = eval(input())
for i in range(n):
    temp = num = eval(input())
    ans = 0
    while temp != 0:
        ans += temp % 10
        temp //= 10
    print('Sum of all digits of %d is %d' %(num, ans))