#Age calculator

#taking inputs
age=int(input("Enter your current age"))
#calculation
future_age=age+5
past_age=age-10
#Showing results
print("\n\nyour current age is",age)
print("\n\n your age will be",future_age,"after 5 years \n\n")
if(past_age<0):
    print("Your age is less than 10 years\n\n")
else:
    print("You were of",past_age,"before 10 year\n\n")
