print("***********************SQUARE**********************")
n=int(input("Enter value of side :"))
x = lambda a : a * a
print("Area of square is : ")
print(x(n))
print("*******************TRIANGLE**********************")
n1=int(input("Enter value of height (h) :"))
n2=int(input("Enter value of base (b) :"))
x1 = lambda a,b : (a * b)/2
print("Area of square is : ")
print(x1(n1,n2))
print("*******************RETANGLE**********************")
n3=int(input("Enter value of length (l) :"))
n4=int(input("Enter value of width (w) :"))
x2 = lambda a,b : a * b
print("Area of square is : ")
print(x2(n3,n4))
