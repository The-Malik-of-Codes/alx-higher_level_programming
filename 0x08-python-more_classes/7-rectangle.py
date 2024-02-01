class Rectangle:
    def __init__(self, width: int = 0, height: int = 0):
        self.width = width
        self.height = height

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, value: int):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, value: int):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self) -> int:
        return self.width * self.height

    def perimeter(self) -> int:
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self) -> str:
        if self.width == 0 or self.height == 0:
            return ""

        rect = []
        for i in range(self.height):
            row = ["#"] * self.width
            rect.append("".join(row))
            if i != self.height - 1:
                rect.append("\n")
        return "\n".join(rect)