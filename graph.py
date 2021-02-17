import graphics
from graphics import circle,rectangle
from graphics.sub import cuboid,sphere
from graphics.circle import *
n=int(input("Enter the value of Radius for finding Circle Area  :"))
print("Area of a circle is : ",circle.area(n))
n1=int(input("Enter the value of Radius for Finding Perimeter of Circle :"))
print("Permeter of a circle is ",circle.perimeter(n1))
n3=int(input("Enter value of length (l) :"))
n4=int(input("Enter value of width (w) :"))
print("Area of a Rectangle  : ",rectangle.area_rectangle(n3,n4))
print("Permeter of a Rectangle : ",rectangle.perimeter_rectangle(n3,n4))
n7=int(input("Enter value of side 1 :"))
n8=int(input("Enter value of side 2 :"))
n9=int(input("Enter value of side 3 :"))
print("Area of a  cuboid  : ",cuboid.area_cuboid(n7,n8,n9))
print("Permeter of a cuboid : ",cuboid.perimeter_cuboid(n7,n8,n9))
n10=int(input("Enter value "))
print("Area of a spere with radius 10 is : ",sphere.area_sphere(n10))
print("Permeter of a spere with radius 10 is ",sphere.perimeter_sphere(n10))