arr = [[0]*3]*3

for i in range(3):
    for j in range(3):
        arr[i][j] = eval(input())

print(max(arr), arr.index(max(arr)))
print(min(arr), arr.index(min(arr)))