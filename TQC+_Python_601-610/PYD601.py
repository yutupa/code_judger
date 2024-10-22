Sum = 0
List = []

for i in range(12):
    List.append(eval(input()))
    if i % 2 == 0:
        Sum += List[i]

for j in range(4):
    print('%3d%3d%3d' %(List[j * 3], List[j * 3 + 1], List[j * 3 + 2]))

print(Sum)

'''
m={}
total=c=0
for i in range(0,12):
   m[i]=int(input())
   if(i%2==0):
     total+=m[i]
for i in range(0,12):
  print('{:>3d}'.format(m[i]),end="")
  c+=1
  if(c==3):
     print()
     c=0
print(total)
'''
