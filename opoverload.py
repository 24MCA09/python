class Rectangle:
    def __init__(self,length,bredth):
        self.length=length
        self.bredth=bredth
    def area(self):
        return self.length*self.bredth

    def __lt__(self,other):
        return self.area() < other.area()
        
print("rectangle 1")
length1=int(input("enter the length"))
bredth1=int(input("enter the bredth"))
rectangle1=Rectangle(length1,bredth1)
print("area 1  = ",rectangle1.area())

print("rectangle 2")
length2=int(input("enter the length"))
bredth2=int(input("enter the bredth"))
rectangle2=Rectangle(length2,bredth2)
print("area = ",rectangle2.area())

if rectangle1 > rectangle2:
    print("Area of Rectangle 1 is larger than Rectangle 2")
elif rectangle1 < rectangle2:
    print("Area of Rectangle 2 is larger than Rectangle 1")
else:
    print("Area of both Rectangles are the same")

