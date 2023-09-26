

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width

rectangle = Rectangle(5, 7)
area = rectangle.compute_area()
print(f"The area of the rectangle is: {area}")
