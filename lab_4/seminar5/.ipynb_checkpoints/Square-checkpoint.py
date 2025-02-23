from Rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"Square with side {self.width} cm"
    def get_info():
        return "This class calculates perimeter and area of the square"
print("Class Square is imported successfully")