


name=input(" Enter your name :  ")

weight=float(input("Weight in (kg): "))

height=float(input("Height in (metre) : "))

bmi=weight/(height ** 2)


# check the bmi 
if bmi<18.5:
    print("Your BMI is " + str(bmi) + " your body is underweight")

elif bmi>18.5 and bmi<25:
    print("Your BMI is " + str(bmi) + "  your body is normal")

elif bmi>25 and bmi<30:
    print("Your BMI is " + str(bmi) + "  your body is overweight")

elif bmi>30:
    print("Your BMI is " + str(bmi) + " you are  obese")

else:
    print("INVALID INPUT")