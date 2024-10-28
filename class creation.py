'''
python classes and objects
create a class called rectangle with two methods
instance variable:length, width
area: calculate area of rectangle
perimeter: calculate the perimeter of rectangle
'''
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
      
    def area(self):
        return self.length*self.width
   
    def perimeter(self):
        return 2*(self.length+self.width)
lenght=float(input("Enter length:"))
width=float(input("Enter width:"))
rect = Rectangle(lenght,width)#instances of a class=objects
print(f"The area is {rect.area()}")
print(f"The perimeter is {rect.perimeter()}")
print(f"Length: {rect.length}")
print(f"width: {rect.width}")
