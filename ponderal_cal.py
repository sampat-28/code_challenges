#Ponderal Index Calculator
#Taking values from user
weight,height=map(float,input("Enter your 1) weight(kg) and 2) height(mtr)").split(" "))
#calculations
temp=weight/height
bmi=temp/height
ponderal=bmi/height
#printing result
print("\nYour Ponderal index is",round(ponderal,2))
