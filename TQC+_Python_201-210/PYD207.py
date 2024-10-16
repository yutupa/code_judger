# TODO

price = eval(input())

if price >= 38000:
    price = price*0.7
elif price >= 28000:
    price = price*0.8
elif price >= 18000:
    price = price*0.9
elif price >= 8000:
    price = price*0.95

print(price)