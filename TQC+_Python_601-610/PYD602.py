sum = 0

for i in range(5):
   n = str(input())
   if(n == 'J'):
       sum += 11
   elif(n == 'Q'):
       sum += 12
   elif(n == 'K'):
       sum += 13
   elif(n == 'A'):
       sum += 1
   else :
       sum += int(n)

print(sum)