class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        area=self.l*self.b
        print("area of rectangle",area)
        return(area)
    def perimeter(self):
        per=2*(self.l+self.b)
        print("perimeter of rectangle",per)
        return(per)
r1=rectangle(4,5)
r2=rectangle(6,5)
a=r1.area()
r1.perimeter()
b=r2.area()
r2.perimeter()
if(a>b):
    print("Rectangle one area is greater",a)
else:
     print("Rectangle two area is greater",b)
