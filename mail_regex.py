f=open("mailid.txt",'rt')
for i in f.readlines():
    print(i)
    a=refind('[a-z]+[0-9]*\.[a-z]+@[a-z]\.[a-z]{2,8}',i)
    if a:
        print(i,"is invalid mail id")
    else:
        (i,"is valid mail id")
f.close()
