LIST = []
num = eval(input())
while num!=-9999:
    LIST.append(num)
    num = eval(input())
TUPLE = tuple(LIST)
print(TUPLE)
print('Length:',len(TUPLE))
print('Max:',max(TUPLE))
print('Min:',min(TUPLE))
print('Sum:',sum(TUPLE))