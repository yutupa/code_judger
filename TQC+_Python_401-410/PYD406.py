while True:

    height = eval(input())
    if height == -9999:
        break
    weight = eval(input())
    if weight == -9999:
        break

    bmi = weight / ((height/100)*(height/100))
    print("BMI: %.2f" %(bmi))

    if bmi < 18.5:
        state = "under weight"
    elif bmi >= 18.5 and bmi < 25:
        state = "normal"
    elif bmi >= 25.0 and bmi < 30:
        state = "over weight"
    elif bmi >= 30:
        state = "fat"

    print("State: %s" %(state))


