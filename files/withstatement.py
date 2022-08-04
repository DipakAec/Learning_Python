with open('demofile1.txt','r') as f:
    a=f.read()
    print(a)

with open('demofile1.txt','w') as f:
    a=f.write("Now i am using with statement")
    print(a)