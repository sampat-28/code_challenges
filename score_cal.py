#Score Calculator
#Taking inputs from users
while True:
    assi1,assi2,assi3=map(int,input("Enter the marks of assignments").split(" "))
    if(assi1>100 or assi2>100 or assi3>100):
        print("assignment marks must be less than or equal to 100")
        continue
    while True:
        exam1,exam2=map(int,input("Enter the marks of exams").split(" "))
        if(exam1>100 or exam2>100):
            print("Marks must be less or equal to 100")
            continue
        else:
            weighted_score=(assi1+assi2+assi3)*0.1+(exam1+exam2)*0.35
            break
    print("Weighted score is:",weighted_score)
    break
