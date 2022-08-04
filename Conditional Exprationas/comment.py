from operator import truediv


text=input("Enter a text\n")

if("make lot of money" in text):
    spam=True
elif("buy now" in text):
    spam=True
elif("subscribe now" in text):
    spam=True
elif("click this" in text):
    spam=True
else:
    spam=False

if(spam==True):
    print("this is spam.")
else:
    print("This is not spam.")