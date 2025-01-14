f1=open("demo.txt","r")
f2=open("demo2.txt","w")
lines=f1.readlines()

for i in range(0,len(lines)):
    if(i%2==0):
        f2.write(lines[i])
f1.close()
f2.close()
f1=open("demo.txt","r")
print(f1.read())

f2=open("demo2.txt","r")
print("odd lines\n",f2.read())
f1.close()
f2.close()