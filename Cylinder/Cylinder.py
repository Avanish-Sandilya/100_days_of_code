class Cylinder:

    pi = 3.14

    def __init__(self, radius=1, height=1):
        self.radius = radius
        self.height = height

    def volume(self):
        return self.pi * (self.radius**2) * self.height

    def surface_area(self):
        return (2*self.pi*(self.radius**2)) + (2*self.pi*self.radius*self.height)



