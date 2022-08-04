from unicodedata import name


namelist=["Arun","Barun","Charan","Kuber","Nitish","Mantu"]
name=input("Give a name to check: ")
if name  in namelist:
    print("your name is in list ",name)

else:
    print("Name out of list.")