while True:
    
    year = eval(input())

    if year == -9999:
        break

    if (year%400 == 0) or (year%4 == 0 and year%100 != 0):
        print('%d is a leap year.' %(year))
    else:
        print('%d is not a leap year.' %(year))
