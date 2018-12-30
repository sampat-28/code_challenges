#pettern
#Taknig values
num=int(input("Enter a number "))
for i in range(1,num*2):
    if(i<=num):
        for j in range (i):   
            print("*",end=(""))
    elif(i>num):
        for j in range((num*2),i
                       ,-1):
            print("*",end=(""))
    print("\r")
