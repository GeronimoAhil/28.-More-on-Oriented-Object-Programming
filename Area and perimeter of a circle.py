class circle:
    def __init__(self, area, perimeter):
        self.area = area
        self.perimeter = perimeter
radius = int(input("Please enter a number greater than 5, but less than 10: "))

pi = 3.14
area = pi*radius**2
perimeter = 2*pi*radius
print("The area of the circle is ",area)
print("The perimeter of the circle is ",perimeter)