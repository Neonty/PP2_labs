class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle with width {self.width} cm and height {self.height} cm"

    def get_info():
        return "This class calculates perimeter and area of the rectangles"
print("Class Rectangle is imported successfully")