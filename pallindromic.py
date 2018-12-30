list_1 = []
str1 = " "
str2 = " "
flag = 0
flag1=0
list_1 = input("enter").split()

for i in list_1:
    str1 = i
    num=int(i)
    if(num<0):
       flag1+=1 
    
    str1 = str1.casefold()
    
    str2 = str1[::-1]
    if (str1 == str2):
        flag+=1
if(flag>=1 and flag1==0):
    print("List is pallindromic")
else:
    print("List is not pallindromic")
