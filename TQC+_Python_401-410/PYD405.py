while True:
    a = eval(input())
    
    if a == -9999:
        break
    
    if (a >= 90) and (a <= 100):
        print("A")
    elif (a >= 80) and (a < 90):
        print("B")
    elif (a >= 70) and (a < 80):
        print("C")
    elif (a >= 60) and (a < 70):
        print("D")
    elif (a >= 0) and (a < 59):
        print("E")