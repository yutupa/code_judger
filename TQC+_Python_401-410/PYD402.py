num_list = []

while True:
    num_list.append(eval(input()))
    if num_list[-1] == 9999:
        break

print(min(num_list))
