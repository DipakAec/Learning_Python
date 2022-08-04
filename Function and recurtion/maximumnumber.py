def max(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

a=int(input("input 1st number: "))
b=int(input("input 2nd number: "))
c=int(input("input 3rd number: "))
m=max(a,b,c)
print("Maximum number is" ,str(m))
