dict1={}
dict2={}

print('Create dict1:')
while True:
    key = input('Key: ')
    if key == 'end':
        break
    dict1[key] = input('Value: ')

print('Create dict2:')
while True:
    key = input('Key: ')
    if key == 'end':
        break
    dict2[key] = input('Value: ')

dict1.update(dict2)
for i in sorted(dict1.keys()):
    print(i+": "+dict1[i])