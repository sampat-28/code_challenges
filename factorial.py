import math
num=int(input("Enter the number of which you want to calculate factorial"))
def factorial(num):
    if num<=1:
        return 1
    else:
        return num*factorial(num-1)
print(factorial)

