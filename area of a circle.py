import math
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return math.pi * self.radius**2
    def circumfrence(self):
        return 2 * math.pi * self.radius 
radius=int(input("Enter length:"))
arc = Circle(radius)

print(f"Area is: {arc.area():.2f}")
print(f"circumfrence is:{arc.circumfrencer():.2f}")
