#BMI Calculator
#Taking values from user
weight,height=map(float,input("Enter your 1) weight(kg) and 2) height(mtr)").split(" "))
#calculations
temp=weight/height
bmi=temp/height
#printing result
print("\nYour BMI is",round(bmi,2))
