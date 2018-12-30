#REVERSE OF  A STRING
#Taking values from user
string=input("Enter the string which you want to print reverse")
test=[]
test1=string
#ittretion to read every character of string
'''This for loop will help to take each entered
character from the string'''
for char in test1[::-1]:
    #print(char,end=(""))
    test.append(char)
    str1=''.join(str(char1) for char1 in test)
#print(test,end=(""))
print("\n",str1)
    
