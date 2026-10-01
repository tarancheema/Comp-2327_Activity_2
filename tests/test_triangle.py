"""Unit tests for the Triangle class."""

import unittest
from shape.triangle import Triangle

__author__ = "Taranpreet Singh"
__version__ = "1.0.0"


class TestTriangle(unittest.TestCase):
    """Test suite for testing the Triangle class."""

    def setUp(self) -> None:
        """Set up standard values for Triangle unit testing."""
        self.color = "Red"
        self.side_1 = 3.0
        self.side_2 = 4.0
        self.side_3 = 5.0
        self.triangle = Triangle(
            self.color, self.side_1, self.side_2, self.side_3
        )

    def test_init_blank_color_raises_value_error(self) -> None:
        """Test __init__ raises ValueError when color is blank."""
        with self.assertRaises(ValueError) as context:
            Triangle("   ", self.side_1, self.side_2, self.side_3)
        self.assertEqual("color cannot be blank", str(context.exception))

    def test_init_side_1_less_than_zero_raises_value_error(self) -> None:
        """Test __init__ raises ValueError when side_1 is less than or equal to zero."""
        with self.assertRaises(ValueError) as context:
            Triangle(self.color, 0.0, self.side_2, self.side_3)
        self.assertEqual(
            "side_1 must be a value greater than zero.", str(context.exception)
        )

    def test_init_side_2_less_than_zero_raises_value_error(self) -> None:
        """Test __init__ raises ValueError when side_2 is less than or equal to zero."""
        with self.assertRaises(ValueError) as context:
            Triangle(self.color, self.side_1, -1.0, self.side_3)
        self.assertEqual(
            "side_2 must be a value greater than zero.", str(context.exception)
        )

    def test_init_side_3_less_than_zero_raises_value_error(self) -> None:
        """Test __init__ raises ValueError when side_3 is less than or equal to zero."""
        with self.assertRaises(ValueError) as context:
            Triangle(self.color, self.side_1, self.side_2, 0.0)
        self.assertEqual(
            "side_3 must be a value greater than zero.", str(context.exception)
        )

    def test_init_invalid_triangle_inequality_raises_value_error(self) -> None:
        """Test __init__ raises ValueError when sides violate Triangle Inequality Theorem."""
        with self.assertRaises(ValueError) as context:
            Triangle(self.color, 1.0, 2.0, 10.0)
        self.assertEqual(
            "The sides do not satisfy the Triangle Inequality Theorem",
            str(context.exception),
        )

    def test_init_valid_attributes_set_successfully(self) -> None:
        """Test valid initialization sets superclass and subclass private attributes."""
        self.assertEqual(self.color, self.triangle._Shape__color)
        self.assertEqual(self.side_1, self.triangle._Triangle__side_1)
        self.assertEqual(self.side_2, self.triangle._Triangle__side_2)
        self.assertEqual(self.side_3, self.triangle._Triangle__side_3)

    def test_color_property_returns_correct_value(self) -> None:
        """Test color property returns the correct color."""
        self.assertEqual(self.color, self.triangle.color)

    def test_area_property_returns_correct_value(self) -> None:
        """Test area property returns the correct calculated area."""
        expected_area = 6.0
        self.assertAlmostEqual(expected_area, self.triangle.area, places=2)

    def test_get_perimeter_returns_correct_value(self) -> None:
        """Test get_perimeter returns the sum of the three sides."""
        expected_perimeter = 12.0
        self.assertEqual(expected_perimeter, self.triangle.get_perimeter())

    def test_str_returns_formatted_string(self) -> None:
        """Test __str__ returns the properly formatted string representation."""
        expected_str = (
            "The shape color is Red.\n"
            "This triangle has three sides with lengths of 3.0, 4.0, and 5.0 centimeters."
        )
        self.assertEqual(expected_str, str(self.triangle))


if __name__ == "__main__":
    unittest.main()