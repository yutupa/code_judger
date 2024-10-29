X = set()
Y = set()

print("Enter group X's subjects:")
Str = input()

while Str != 'end':
    X.add(Str)
    Str = input()

print("Enter group Y's subjects:")
Str = input()

while Str != 'end':
    Y.add(Str)
    Str = input()

# print(sorted(X | Y))
# print(sorted(X & Y))
# print(sorted(Y - X))
# print(sorted(X ^ Y))

print(sorted(X.union(Y)))
print(sorted(X.intersection(Y)))
print(sorted(Y.difference(X)))
print(sorted(X.symmetric_difference(Y)))