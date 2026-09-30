"""Module containing the abstract Shape base class."""

from abc import ABC, abstractmethod

__author__ = "Taranpreet Singh"
__version__ = "1.0.0"


class Shape(ABC):
    """Abstract base class representing a geometric shape."""

    def __init__(self, color: str) -> None:
        """Initialize the shape with a color.

        Args:
            color (str): The color of the shape.

        Raises:
            ValueError: If color is blank after stripping whitespace.
        """
        if len(color.strip()) == 0:
            raise ValueError("color cannot be blank")

        self.__color = color.strip()

    @property
    def color(self) -> str:
        """Get the color of the shape.

        Returns:
            str: The color of the shape.
        """
        return self.__color

    @property
    @abstractmethod
    def area(self) -> float:
        """Get the area of the shape.

        Returns:
            float: The area of the shape.
        """
        pass

    @abstractmethod
    def get_perimeter(self) -> float:
        """Calculate and return the perimeter of the shape.

        Returns:
            float: The perimeter of the shape.
        """
        pass

    def __str__(self) -> str:
        """Return a string representation of the shape.

        Returns:
            str: Formatted string indicating the shape's color.
        """
        return f"The shape color is {self.__color}."