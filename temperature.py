class Temperature:
    def convertFahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is {fahrenheit}°F")

    def convertCelsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is {celsius}°C")

temp = Temperature()
temp.convertFahrenheit(25) 
temp.convertCelsius(77)      


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.14159 * (self.radius ** 2)
        print(f"Area of the circle with radius {self.radius} is {area}")

    def circumference(self):
        circumference = 2 * 3.14159 * self.radius
        print(f"Circumference of the circle with radius {self.radius} is {circumference}")

circle = Circle(5)
circle.area()            
circle.circumference()  
