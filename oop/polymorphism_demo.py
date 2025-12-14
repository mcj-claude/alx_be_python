import math


class Shape:
    """
    Base class representing a generic shape.
    The area() method raises NotImplementedError to indicate that 
    derived classes need to override this method.
    """
    def area(self):
        """
        Calculate the area of the shapeImplementedError to enforce.
        Raises Not implementation in derived classes.
        """
        raise NotImplementedError("Subclasses must override this method")


class Rectangle(Shape):
    """
    Derived class representing a rectangle.
    Inherits from Shape and overrides the area() method.
    """
    def __init__(self, length, width):
        """
        Initialize a Rectangle instance with length and width.
        """
        self.length = length
        self.width = width
    
    def area(self):
        """
        Calculate the rectangle's area using the formula: length × width.
        """
        return self.length * self.width


class Circle(Shape):
    """
    Derived class representing a circle.
    Inherits from Shape and overrides the area() method.
    """
    def __init__(self, radius):
        """
        Initialize a Circle instance with radius.
        """
        self.radius = radius
    
    def area(self):
        """
        Calculate the circle's area using the formula: π × radius²
        Uses math.pi for the value of π.
        """
        return math.pi * (self.radius ** 2)