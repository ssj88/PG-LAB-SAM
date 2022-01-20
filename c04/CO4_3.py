class rectangle:

  def __init__(self,l,b):
    self.__length=l
    self.__breadth=b

  def area(self):
    self.area=self.__length*self.__breadth
    print("Area=",self.area)

  def __lt__(self,second):
   if self.area < second.area:
    return True
   else:
    return False

print(" Rectangle 1")
len1=int(input("Enter length:"))
bread1=int(input("Enter breadth:"))
obj1=rectangle(len1,bread1)
obj1.area()

print(" Rectangle 2")
len2=int(input("Enter length:"))
bread2=int(input("Enter breadth:"))
obj2=rectangle(len2,bread2)
obj2.area()

if obj1 < obj2 :
 print(" 2nd rectangle  area large:")
else:
 print(" 1st rectangle area large:")