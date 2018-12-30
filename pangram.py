import re
string1=input("Enter the string")
string1=string1.lower()
flag=0
set1=(set(string1))
for check in set1:
    check1=re.search('[a-z]',check)
    if check1:
       flag+=1
if(flag==26):
    print("PANGRAM")
else:
    print("NOT PANGAM")

