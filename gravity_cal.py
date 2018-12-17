#Gravity Calculator
#Taking values from user
while True:
    distance=int(input("Enter the distance of object in metres from the ground "))
    if(distance<481):
        print("Enter the distance greater than 491 metre")
        continue
    else:
        print ("here is the result")
#Calculations
    time=10
    acceleration=9.81
    covered_dis=(acceleration*time*time)/2
    rem_dis=distance-covered_dis
#printing results
    print("Object will be at the distance of",round(rem_dis,2),"metres from ground after falling of",time,"seconds")
    break
