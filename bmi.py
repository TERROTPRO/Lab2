#Exercise 1:

def calculate_bmi(height, weight):
    print("Height= ",str(height))
    print("Weight= ",str(weight))
    bmi = weight / (height ** 2)
    print("BMI= ",str(f"{bmi:.2f}"))

    if bmi < 18.5:
        print("Under Weight")    
    elif bmi >= 18.5 and bmi <= 25:
        print("Normal weight")
    else:
        print("Over Weight")

calculate_bmi(1.73, 57)

#Own Exercise (Input from user):

Height = float(input("Enter your height in meters: "))
Weight = float(input("Enter your weight in kilograms: "))

bmi = Weight / (Height ** 2)
print("Your BMI is: ", str(f"{bmi:.2f}"))
if bmi < 18.5:
        print("Under Weight")    
elif bmi >= 18.5 and bmi <= 25:
        print("Normal weight")
else:
        print("Over Weight")




