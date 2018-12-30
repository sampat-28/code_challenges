#Bricks
#Taking values
small_bricks,big_bricks,length=map(int,input("Enter the number of small bricks, big briks and length of wall").split(" "))
#calculations
temp=big_bricks*5
temp1=temp+small_bricks
#Conditions check and itterations
if(temp1>=length):
    while(length!=0):
        if(big_bricks!=0 and length>=5):
            length=length-5
            big_bricks=big_bricks-1
        elif(small_bricks!=0 and length>=1):
            length=length-1
            small_bricks=small_bricks-1
        else:
            break
        if(length==0):
#Printing results
            print("True")
else:
    print("False")
