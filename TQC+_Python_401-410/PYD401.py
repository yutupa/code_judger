a = []

for i in range(10):
    a.append(eval(input()))

'''
minimum = a[0]
for i in range(10):
    if a[i] < minimum:
        minimum = a[i]

print(minimum)
'''

print(min(a))
