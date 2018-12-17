#Temprature Calculator
degree=float(input("Enter the temprature of city"))
fahrenheit=degree*9/5+32
kelvin=degree+273.15
#printing the results
print("\nTemprature in fahrenheit is ",round(fahrenheit,2))
print("\nTemprature in kelvin is",round(kelvin,2))
