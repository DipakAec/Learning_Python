from asyncore import read


f = open("myfile.txt", "r")
data=f.readline()
print(data)

data=f.readline()
print(data)

f.close()