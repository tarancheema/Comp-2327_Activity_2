"""Module containing the Triangle subclass."""

import math
from shape.shape import Shape

__author__ = "Taranpreet Singh"
__version__ = "1.0.0"


class Triangle(Shape):
    """Represents a triangle shape, inheriting from Shape."""

    def __init__(self, color: str, side_1: float, side_2: float, side_3: float) -> None:
        """Initialize a triangle instance with color and three side lengths.

        Args:
            color (str): The color of the triangle.
            side_1 (float): The length of the first side in centimeters.
            side_2 (float): The length of the second side in centimeters.
            side_3 (float): The length of the third side in centimeters.

        Raises:
            ValueError: If side_1, side_2, or side_3 is less than or equal to zero,
                or if the sides do not satisfy the Triangle Inequality Theorem.
        """
        super().__init__(color)

        if side_1 <= 0:
            raise ValueError("side_1 must be a value greater than zero.")

        if side_2 <= 0:
            raise ValueError("side_2 must be a value greater than zero.")

        if side_3 <= 0:
            raise ValueError("side_3 must be a value greater than zero.")

        if not (
            side_1 + side_2 > side_3
            and side_1 + side_3 > side_2
            and side_2 + side_3 > side_1
        ):
            raise ValueError(
                "The sides do not satisfy the Triangle Inequality Theorem"
            )

        self.__side_1 = side_1
        self.__side_2 = side_2
        self.__side_3 = side_3

    @property
    def area(self) -> float:
        """Calculate and return the area of the triangle using Heron's formula.

        Returns:
            float: The area of the triangle.
        """
        sp = (self.__side_1 + self.__side_2 + self.__side_3) / 2
        return math.sqrt(
            sp
            * (sp - self.__side_1)
            * (sp - self.__side_2)
            * (sp - self.__side_3)
        )

    def get_perimeter(self) -> float:
        """Calculate and return the perimeter of the triangle.

        Returns:
            float: The perimeter of the triangle.
        """
        return self.__side_1 + self.__side_2 + self.__side_3

    def __str__(self) -> str:
        """Return the formatted string representation of the triangle.

        Returns:
            str: Description of the triangle and its side lengths.
        """
        return (
            f"{super().__str__()}\n"
            f"This triangle has three sides with lengths of "
            f"{self.__side_1}, {self.__side_2}, and {self.__side_3} centimeters."
        )