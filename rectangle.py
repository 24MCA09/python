class Rectangle:
    def __init__(self,length,bredth):
        self.length=length
        self.bredth=bredth
    def Calculate_area(self):
        return self.length*self.bredth
    def Calculate_perimeter(self):
        return 2*(length+bredth)
    
print("rectangle 1")
length=int(input("enter the length"))
bredth=int(input("enter the bredth"))
rectangle=Rectangle(length,bredth)
area1=rectangle.Calculate_area()
print("area = ",rectangle.Calculate_area())
print("perimeter = ",rectangle.Calculate_perimeter())

print("rectangle 2")
length2=int(input("enter the length"))
bredth2=int(input("enter the bredth"))
rectangle=Rectangle(length2,bredth2)
area2=rectangle.Calculate_area()
print("area = ",rectangle.Calculate_area())
print("perimeter = ",rectangle.Calculate_perimeter())


if area1 > area2:
    print('Area of Rectangle 1 is larger than Rectangle 2')
elif area1==area2:
    print('Area of both Rectangle are same')
else:
    print('Area of Rectangle 2 is larger than Rectangle 1')
