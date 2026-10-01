"""Module containing the Rectangle subclass."""

from shape.shape import Shape

__author__ = "Taranpreet Singh"
__version__ = "1.0.0"


class Rectangle(Shape):
    """Represents a rectangle shape, inheriting from Shape."""

    def __init__(self, color: str, length: float, width: float) -> None:
        """Initialize a rectangle instance with color, length, and width.

        Args:
            color (str): The color of the rectangle.
            length (float): The length of opposing sides in centimeters.
            width (float): The width of opposing sides in centimeters.

        Raises:
            ValueError: If length or width is less than or equal to zero.
        """
        super().__init__(color)

        if length <= 0:
            raise ValueError("length must be a value greater than zero.")

        if width <= 0:
            raise ValueError("width must be a value greater than zero.")

        self.__length = length
        self.__width = width

    @property
    def area(self) -> float:
        """Calculate and return the area of the rectangle.

        Returns:
            float: The area of the rectangle (length * width).
        """
        return self.__length * self.__width

    def get_perimeter(self) -> float:
        """Calculate and return the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle (length * 2 + width * 2).
        """
        return (self.__length * 2) + (self.__width * 2)

    def __str__(self) -> str:
        """Return the formatted string representation of the rectangle.

        Returns:
            str: Description of the rectangle, its length, and width.
        """
        return (
            f"{super().__str__()}\n"
            f"This rectangle has a length of {self.__length}cm and a width of {self.__width}cm."
        )