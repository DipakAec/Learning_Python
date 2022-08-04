a=int(input("Enter frist number: "))
b=int(input ("Enter second number: "))
c=int(input ("Enter third number: "))
d=int(input ("Enter fourth number: "))

numlist=[a,b,c,d]

if(a>b):
    f1=a
else:
    f1=b

if(c>d):
    f2=c
else:
    f2=d

if(f1>f2):
    print("The greatest number is: ",f1)
else:
    print("The greatest number is",f2)
