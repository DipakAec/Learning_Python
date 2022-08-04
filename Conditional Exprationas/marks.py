a=int(input ("Enter number of subject1(out of 100): "))
b=int(input ("Enter number of subject2(out of 100): "))
c=int(input ("Enter number of subject3(out of 100): "))



marks=((a+b+c)/300)*100

if(a<33 or b<33 or c<33):
    print("You are faild due to less marks in a subject")

elif(marks<40):
    print("You are failed due to overall less marks ")

else:
    print("Congratulation! You passed")

