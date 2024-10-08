amount = eval(input())
rate = eval(input())
month = eval(input())

print('%s \t  %s' % ('Month', 'Amount'))

for i in range(1, month+1):
    amount = amount + amount * rate / 1200
    print('%3d \t %.2f' % (i, amount))

