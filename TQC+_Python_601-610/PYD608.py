
# arr = [[0]*3]*3 #trap
arr = [ [0]*3 for i in range(3)]

for i in range(3):
    for j in range(3):
        arr[i][j] = eval(input())
        
max = arr[0][0]
max_index_i = 0
max_index_j = 0
min = arr[0][0]
min_index_i = 0
min_index_j = 0

for rows in arr:
    for cols in rows:
        if cols > max:
            max = cols
            max_index_i = arr.index(rows)
            max_index_j = rows.index(cols)
        if cols < min:
            min = cols
            min_index_i = arr.index(rows)
            min_index_j = rows.index(cols)

print("max: %d in (%d, %d)" %(max, max_index_i, max_index_j))
print("min: %d in (%d, %d)" %(min, min_index_i, min_index_j))