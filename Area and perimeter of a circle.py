class circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return pi*radius**2
    def perimeter(self):
        return 2*pi*radius
radius = int(input("Please enter a number greater than 5, but less than 10: "))
c = circle(radius)
pi = 3.14
print("The area of the circle is ",c.area())
print("The perimeter of the circle is ",c.perimeter())