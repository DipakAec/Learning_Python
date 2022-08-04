from asyncore import read


f = open("myfile.txt", "r")
data=f.read()
print(data)
f.close()