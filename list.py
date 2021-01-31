number=int(input("Enter Total number of elements in list : "))
lists=[]
for i in range(number):
    value=int(input("Enter a number :"))
    lists.append(value)
    
result = [each for each in lists if each>0]
print(result)
