from tomlkit import date


letter=''' Dear |NAME| ,
you are selected in ABC coding house
Have a Good Day
|DATE|'''
name=input("Enter a name: ")
date=input("Enter a date")
letter=letter.replace("|NAME|",name)
letter=letter.replace("|DATE|",date)
print(letter)