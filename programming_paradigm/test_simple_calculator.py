import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Test class for SimpleCalculator with comprehensive test cases."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition_basic(self):
        """Test basic addition operations."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(7, 8), 15)

    def test_addition_with_negatives(self):
        """Test addition with negative numbers."""
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(10, -3), 7)
        self.assertEqual(self.calc.add(-10, 5), -5)

    def test_addition_with_floats(self):
        """Test addition with floating point numbers."""
        self.assertEqual(self.calc.add(2.5, 3.1), 5.6)
        self.assertEqual(self.calc.add(-1.5, 2.5), 1.0)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7)

    def test_subtraction_basic(self):
        """Test basic subtraction operations."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(7, 8), -1)

    def test_subtraction_with_negatives(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(10, -3), 13)
        self.assertEqual(self.calc.subtract(-10, 5), -15)

    def test_subtraction_with_floats(self):
        """Test subtraction with floating point numbers."""
        self.assertEqual(self.calc.subtract(5.5, 2.1), 3.4)
        self.assertEqual(self.calc.subtract(-1.5, 2.5), -4.0)
        self.assertAlmostEqual(self.calc.subtract(0.3, 0.1), 0.2, places=7)

    def test_multiplication_basic(self):
        """Test basic multiplication operations."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(10, 5), 50)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(7, 8), 56)

    def test_multiplication_with_negatives(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-5, -3), 15)
        self.assertEqual(self.calc.multiply(10, -3), -30)
        self.assertEqual(self.calc.multiply(-10, 5), -50)

    def test_multiplication_with_floats(self):
        """Test multiplication with floating point numbers."""
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)
        self.assertEqual(self.calc.multiply(-1.5, 2.5), -3.75)
        self.assertEqual(self.calc.multiply(0.5, 0.5), 0.25)

    def test_division_basic(self):
        """Test basic division operations."""
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(15, 3), 5)
        self.assertEqual(self.calc.divide(7, 2), 3.5)

    def test_division_with_negatives(self):
        """Test division with negative numbers."""
        self.assertEqual(self.calc.divide(-6, 2), -3)
        self.assertEqual(self.calc.divide(6, -2), -3)
        self.assertEqual(self.calc.divide(-6, -2), 3)
        self.assertEqual(self.calc.divide(-10, 4), -2.5)

    def test_division_with_floats(self):
        """Test division with floating point numbers."""
        self.assertEqual(self.calc.divide(5.0, 2.0), 2.5)
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertEqual(self.calc.divide(1.0, 3.0), 0.3333333333333333)

    def test_division_by_zero(self):
        """Test division by zero edge case."""
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(10.5, 0))

    def test_division_zero_dividend(self):
        """Test division when dividend is zero."""
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(0, -5), 0)
        self.assertEqual(self.calc.divide(0.0, 2.0), 0.0)

    def test_large_numbers(self):
        """Test operations with large numbers."""
        self.assertEqual(self.calc.add(1000000, 2000000), 3000000)
        self.assertEqual(self.calc.subtract(5000000, 1000000), 4000000)
        self.assertEqual(self.calc.multiply(1000, 2000), 2000000)
        self.assertEqual(self.calc.divide(1000000, 1000), 1000)

    def test_commutative_property_addition(self):
        """Test that addition is commutative: a + b = b + a."""
        self.assertEqual(self.calc.add(5, 10), self.calc.add(10, 5))
        self.assertEqual(self.calc.add(-3, 7), self.calc.add(7, -3))
        self.assertEqual(self.calc.add(2.5, 3.1), self.calc.add(3.1, 2.5))

    def test_commutative_property_multiplication(self):
        """Test that multiplication is commutative: a * b = b * a."""
        self.assertEqual(self.calc.multiply(5, 10), self.calc.multiply(10, 5))
        self.assertEqual(self.calc.multiply(-3, 7), self.calc.multiply(7, -3))
        self.assertEqual(self.calc.multiply(2.5, 3.0), self.calc.multiply(3.0, 2.5))

    def test_identity_properties(self):
        """Test identity properties: a + 0 = a and a * 1 = a."""
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(-3, 0), -3)
        self.assertEqual(self.calc.add(2.5, 0), 2.5)
        
        self.assertEqual(self.calc.multiply(5, 1), 5)
        self.assertEqual(self.calc.multiply(-3, 1), -3)
        self.assertEqual(self.calc.multiply(2.5, 1), 2.5)

    def test_zero_properties(self):
        """Test zero properties: a * 0 = 0 and 0 / a = 0 (when a ≠ 0)."""
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(-3, 0), 0)
        self.assertEqual(self.calc.multiply(2.5, 0), 0)
        
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(0, -3), 0)
        self.assertEqual(self.calc.divide(0, 2.5), 0)


if __name__ == '__main__':
    unittest.main()