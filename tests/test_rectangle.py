"""Unit tests for the Rectangle class."""

import unittest
from shape.rectangle import Rectangle

__author__ = "Taranpreet Singh"
__version__ = "1.0.0"


class TestRectangle(unittest.TestCase):
    """Test suite for testing the Rectangle class."""

    def setUp(self) -> None:
        """Set up standard values for Rectangle unit testing."""
        self.color = "Red"
        self.length = 5.0
        self.width = 6.0
        self.rectangle = Rectangle(self.color, self.length, self.width)

    def test_init_blank_color_raises_value_error(self) -> None:
        """Test __init__ raises ValueError when color is blank."""
        with self.assertRaises(ValueError) as context:
            Rectangle("   ", self.length, self.width)
        self.assertEqual("color cannot be blank", str(context.exception))

    def test_init_length_less_than_zero_raises_value_error(self) -> None:
        """Test __init__ raises ValueError when length is less than or equal to zero."""
        with self.assertRaises(ValueError) as context:
            Rectangle(self.color, 0.0, self.width)
        self.assertEqual(
            "length must be a value greater than zero.", str(context.exception)
        )

    def test_init_width_less_than_zero_raises_value_error(self) -> None:
        """Test __init__ raises ValueError when width is less than or equal to zero."""
        with self.assertRaises(ValueError) as context:
            Rectangle(self.color, self.length, -1.0)
        self.assertEqual(
            "width must be a value greater than zero.", str(context.exception)
        )

    def test_init_valid_attributes_set_successfully(self) -> None:
        """Test valid initialization sets superclass and subclass private attributes."""
        self.assertEqual(self.color, self.rectangle._Shape__color)
        self.assertEqual(self.length, self.rectangle._Rectangle__length)
        self.assertEqual(self.width, self.rectangle._Rectangle__width)

    def test_color_property_returns_correct_value(self) -> None:
        """Test color property returns the correct color."""
        self.assertEqual(self.color, self.rectangle.color)

    def test_area_property_returns_correct_value(self) -> None:
        """Test area property returns the correct calculated area."""
        expected_area = 30.0
        self.assertEqual(expected_area, self.rectangle.area)

    def test_get_perimeter_returns_correct_value(self) -> None:
        """Test get_perimeter returns the correct perimeter."""
        expected_perimeter = 22.0
        self.assertEqual(expected_perimeter, self.rectangle.get_perimeter())

    def test_str_returns_formatted_string(self) -> None:
        """Test __str__ returns the properly formatted string representation."""
        expected_str = (
            "The shape color is Red.\n"
            "This rectangle has a length of 5.0cm and a width of 6.0cm."
        )
        self.assertEqual(expected_str, str(self.rectangle))


if __name__ == "__main__":
    unittest.main()