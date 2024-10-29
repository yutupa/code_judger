L=[]
for w in range(4):
  print("Week %d:"%(w+1))
  for D in range(3):
    x=eval(input("Day %d:"%(D+1)))
    L.append(x)
 
A=sum(L)/len(L)
print("Average: %.2f"%A)
if max(L) % 1 == 0:
  print("Highest:",int(max(L)))
else:
  print("Highest:",max(L))


if min(L) % 1 == 0:
  print("Lowest:",int(min(L)))
else:
  print("Lowest:",min(L))