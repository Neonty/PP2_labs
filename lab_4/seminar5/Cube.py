from Square import Square

class Cube(Square):
    def __init__(self, side):
        super().__init__(side)

    def get_surface_area(self):
        return 6 * (self.width ** 2)

    def get_volume(self):
        return self.width ** 3

    def __str__(self):
        return f"Cube with side {self.width} cm"
    def get_info():
        return "This class calculates surface area and volume of the cube"
print("Class Cube is imported successfully")