file=open("demo.txt","r")
l=[i.split() for i in file]
print(l)
file.close()