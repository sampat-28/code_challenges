#Heart Rate Calculator
#Taking values
age=int(input("Enter your age in years"))
#calculations
max_rate=220-age
lower_end=max_rate*0.7
higher_end=max_rate*0.85
#printing results
print("Lower end heart rate is",int(lower_end))
print("Higher end heart rate is",int(higher_end))
