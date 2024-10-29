tuple1 = ()
num = eval(input('Create tuple1:\n'))
while num !=-9999:
    tuple1 +=(num,)
    num = eval(input())
tuple2 = ()
num = eval(input('Create tuple2:\n'))
while num !=-9999:
    tuple2 +=(num,)
    num = eval(input())
tuple1 += tuple2
print('Combined tuple before sorting:',tuple1)
LIST = list(tuple1)
LIST.sort()
print('Combined list after sorting:',LIST)