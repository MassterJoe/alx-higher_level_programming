#!/usr/bin/python3
"""Rectangle class inheriting from base class"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle
            height (int): The height of the new rectangle
            x and y: x cordinate and y cordinate of the
            new rectangle respectively
        Raises:
            TypeError: If the width, height, x or y is not an int
            ValueError: if the width or height <= 0
                        if x or y < 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set/get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("Width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ It returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """print the rectangle using the # character """
        for y in range(self.y):
            print("")
        for i in range(self.height):
            k = ""
            for x in range(self.x):
                k = k + " "
            m = ""
            for j in range(self.width):
                m = m + "#"
            if not self.x and not self.y:
                print(m)
            else:
                print(k, m)

    def __str__(self):
        """returns the __str__ representation"""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """update the rectangle
        args:
            *args (int): new attribute value
            - 1st argument is id
            - 2nd argument is width
            - 3rd argument is height
            - 4th argument is x
            - 5th argument is y
        """
        a = 0
        if args and len(args) != 0:
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """This function returns a dictionary representation
        of a Rectangle object """
        return {
            "id": self.id,
            "width": self.width,
            "x": self.x,
            "y": self.y
        }
