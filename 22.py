class rectangle:
    area = 0
    def __init__(self,length,width):
        self.__length = length
        self.__width = width
    def calc_area(self):
        self.area = self.__length*self.__width
        print("Area is  :",self.area)
    def __lt__(self,second):
        if self.area < second.area:
            return True
        else:
            return False
print("**********************RETANGLE COMPARISON***********************")
length1= int(input("Enter length of the rectangle 1 : "))
width1 = int(input("Enter width of the rectangle  1 : "))
length2 = int(input("Enter length of the rectangle  2  : "))
width2 = int(input("Enter width of the rectangle  2 : "))
obj1 = rectangle(length1,width1)
obj2 = rectangle(length2,width2)
obj1.calc_area()
obj2.calc_area()

if obj1 < obj2:
        print("Rectangle two is large")
else:
        print("Rectangle one is large or these are equal")