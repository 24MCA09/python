# (C01) 9. Create a string from given string where first and last characters exchanged.[eg: python -> nythop]

s=input("Enter a String : ")
f=s[0]
l=s[-1:]
print("New String : ",l+s[1:-1]+f)

#(CO1)2.Display future leap years from current year to a final year entered by user.

year1=int(input("enter starting year "))
year2=int(input("enter final year "))
for x in range(year1,year2):
  if (x%4==0 and x%100!=0 )or x%400==0:
    print("leap year ",x)
    
    
# (C01) 8. Get a string from an input string where all occurrences of first character replaced with ‘$’, except first #character. [eg: onion -> oni$n]

l=input("Enter a String : ")
f=l[0]
l1=l[1:].replace(f, "$")
print(f," replaced with $")
print("New String : ",f+l1)


# (C01) 7.Enter 2 lists of integers.Check 
# (a) Whether list are of same length 
# (b) whether list sums to same value 
# (c) whether any value occur in both

l=input("enter list1 of integers seperated by spaces ")
l1=[int(num) for num in l.split()]
m=input("enter list2 of integers seperated by spaces ")
l2=[int(num) for num in m.split()]
print(l1)
print(l2)
a=len(l1)
b=len(l2)
if a==b:
  print("list are of same length")
else:
  print("list are not of same length")
c=sum(l1)
d=sum(l2)
if c==d:
  print("sum of list elements same")
else:
  print("sum of list elements not same")
l3=[x for x in l1 if x in l2]
print("value common in both list ",l3)



# (C01) 6. Store a list of first names. Count the occurrences of ‘a’ within the list

import math
l=[i for i in input("Enter List : ").split()]
print(l)
count=0
for i in l:
    count+= i.lower().count('a')
print("Count of Letter A : ",count)



# (C01) 5.Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead.

u=input("enter list of integers seperated by spaces ")
numbers=u.split()
print(numbers)
#numbers=[int(num) for num in u.split()]
result=[]
for num in numbers:
  numbers=int(num)
  print(numbers)
  if numbers > 100:
    result.append("over")
  else:
    result.append(numbers)
print("new list")
print(result)


# (C01) 4. Count the occurrences of each word in a line of text.

l=input("Enter a line : ")
words = l.split()
res = {}
for word in words:
    word = word.lower() 
    if word in res:
        res[word] += 1
    else:
        res[word] = 1
for word, count in res.items():
    print(f"'{word}': {count}")
    
    
# (C01) 3.(d).List ordinal value of each element of a word (Hint: use ord() to get ordinal values)

word=input("Enter a word : ")
ordinal_values = [ord(char) for char in word]
print(f"The ordinal values of the characters in the word '{word}' are: {ordinal_values}")

    
(C01) 3.(c).Form a list of vowels selected from a given word.

l=input("enter a word ")
l1=[x for x in l]
print(l1)
print("vowels")
l2=["a","e","i","o","u","A","E","I","O","U"]
l3=[x for x in l1 if x in l2]
print(l3)


# (C01) 3.(b).Square of N numbers.

l=input("enter list of integers seperated by spaces ")
l1=[int(num) for num in l.split()]
print(l1)
print("square of numbers")
l2=[(num*num) for num in l1]
print(l2)


# (C01) 3.(a).Generate positive list of numbers from a given list of integers.

l=input("enter list of integers seperated by spaces ")
l1=[int(num) for num in l.split()]
pl=[num for num in l1 if num>0]
print("list of positive numbers are ",pl)



# (C01)  19.Find gcd of 2 numbers.

import math
x=int(input("enter num1 "))
y=int(input("enter num2 "))
print("gcd is ",math.gcd(x,y))


# (C01)  18.Merge two dictionaries.

d1={"apple":"red","orange":"orange","banana":"yellow","kiwi":"green"}
d2={"pineapple":"yelow","mango":"green"}
print("Dict 1 -",d1)
print("Dict 2 -",d2)
d1.update(d2)
print(d1)
print(d1|d2)

file=input("Enter File Name : ")
temp=file.split(".")
ext= temp[-1] if len(temp) > 1 else ""
print("Extension : ",ext)

x=int(input("Enter an Integer : "))
n1 = int(f"{x}") # nn
n2 = int(f"{x}{x}") # nn
n3 = int(f"{x}{x}{x}") #nnn
print(n1,"+",n2,"+",n3," = ",n1+n2+n3)

ol=[int(i) for i in input("enter the integers ").split()]
print("list before ",ol)
newlist=[i for i in ol if i%2==0]
print("list after removing even numbers ",newlist)


num=int(input("Enter a num"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)


# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0
seris=[]
if nterms <= 0:
  print("Please enter a positive integer")
elif nterms == 1:
  print("Fibonacci sequence upto",nterms,":")
  print(n1)
# generate fibonacci sequence
else:
  for i in range(nterms):
      seris.append(n1)
      nth = n1 + n2
      # update values
      n1 = n2
      n2 = nth
  print("Fibonacci sequence:",seris)
       
   
list=[int(i) for i in input("enter numbers").split()]
print(sum(list))


n= int(input("Enter a number :"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print(" ")


from collections import Counter
s = input("Enter a string: ")
char_frequency = Counter(s)
print("Character Frequency:")
for char, freq in char_frequency.items():
    print(f"'{char}': {freq}")


s=input("Enter a string :")
a=s[-3:]
if a=='ing':
    print(s+'ly')
else:
    print(s+'ing')


words = input("Enter a list of words : ").split()
longest = max(len(word) for word in words)
print("Length of the longest word:", longest)



for i in range(5):
    for j in range(i + 1):
        print("*", end=" ")
    print()
for i in range(5):
    for j in range(5-i-1):
        print("*", end=" ")
    print()


for i in range(5):
    for j in range(i+1):
        print('*',end=" ")
    print(" ")
    
num = int(input("Enter a number: "))
factors = [i for i in range(1, num + 1) if num % i == 0]
print("Factors of the number:", factors)




area1=lambda a :a*a
area2=lambda l,b :l*b
area3=lambda b,h :0.5*b*h
s=int(input("enter side of square "))
print("area of square= ",area1(s))
l=int(input("enter length of rectangle "))
b=int(input("enter breadth of rectangle "))
print("area of rectangle= ",area2(l,b))
p=int(input("enter base of triangle "))
h=int(input("enter height of triangle "))
print("area of triangle= ",area3(p,h))











co3








from graphics import rectangle, circle
from graphics threeD import cuboid, sphere
#rectangle module
length=int(input("enter length of rectangle: "))
width=int(input("enter width of rectangle: "))
print("area of rectangle= ",rectangle.area(length,width))
print("perimeter of rectangle= ",rectangle.perimeter(length,width))
print()
#circle module
radius=int(input("enter radius of circle: "))
print("area of circle= ",circle.area(radius))
print("perimeter of circle= ",circle.perimeter(radius))
print()
#cuboid module
clength=int(input("enter length of cuboid: "))
cwidth=int(input("enter width of cuboid: "))



















