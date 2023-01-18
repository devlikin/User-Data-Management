class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def scale(self, scale):
        self.width = self.width * scale
        self.height = self.height * scale

    #    def __repr__(self):
    #        string = str(self.height) + " " + str(self.width)
    #        return string

    def __hash__(self):
        return self.width + self.height


rectangle1 = Rectangle(3, 4)
print(rectangle1.width)
