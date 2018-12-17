import re
can=[]
cn=input("Enter the card number")
for i in range(cn):
    cnn=re.match('^\d[0-9]{4}[a-z]{4}',i)
if cn:
    print("valid card number")
else:
    print("Invalid card number")
