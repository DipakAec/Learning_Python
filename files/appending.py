f = open("demofile1.txt", "w") # a for append and w wtite fully new text in file(old text will lost)
f.write("I am create this file by using write")
f.close()

#open and read the file after the appending:
f = open("demofile1.txt", "r")
print(f.read())