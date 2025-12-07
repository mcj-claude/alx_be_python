import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Test class for SimpleCalculator with comprehensive test cases."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method with various scenarios."""
        # Basic addition
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(7, 8), 15)
        
        # Addition with negatives
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(10, -3), 7)
        self.assertEqual(self.calc.add(-10, 5), -5)
        
        # Addition with floats
        self.assertEqual(self.calc.add(2.5, 3.1), 5.6)
        self.assertEqual(self.calc.add(-1.5, 2.5), 1.0)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7)

    def test_subtraction(self):
        """Test the subtraction method with various scenarios."""
        # Basic subtraction
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(7, 8), -1)
        
        # Subtraction with negatives
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(10, -3), 13)
        self.assertEqual(self.calc.subtract(-10, 5), -15)
        
        # Subtraction with floats
        self.assertEqual(self.calc.subtract(5.5, 2.1), 3.4)
        self.assertEqual(self.calc.subtract(-1.5, 2.5), -4.0)
        self.assertAlmostEqual(self.calc.subtract(0.3, 0.1), 0.2, places=7)

    def test_multiplication(self):
        """Test the multiplication method with various scenarios."""
        # Basic multiplication
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(10, 5), 50)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(7, 8), 56)
        
        # Multiplication with negatives
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-5, -3), 15)
        self.assertEqual(self.calc.multiply(10, -3), -30)
        self.assertEqual(self.calc.multiply(-10, 5), -50)
        
        # Multiplication with floats
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)
        self.assertEqual(self.calc.multiply(-1.5, 2.5), -3.75)
        self.assertEqual(self.calc.multiply(0.5, 0.5), 0.25)

    def test_division(self):
        """Test the division method with various scenarios."""
        # Basic division
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(15, 3), 5)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        
        # Division with negatives
        self.assertEqual(self.calc.divide(-6, 2), -3)
        self.assertEqual(self.calc.divide(6, -2), -3)
        self.assertEqual(self.calc.divide(-6, -2), 3)
        self.assertEqual(self.calc.divide(-10, 4), -2.5)
        
        # Division with floats
        self.assertEqual(self.calc.divide(5.0, 2.0), 2.5)
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertEqual(self.calc.divide(1.0, 3.0), 0.3333333333333333)
        
        # Division by zero (edge case)
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(10.5, 0))
        
        # Division when dividend is zero
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(0, -5), 0)
        self.assertEqual(self.calc.divide(0.0, 2.0), 0.0)

    def test_edge_cases(self):
        """Test additional edge cases and mathematical properties."""
        # Large numbers
        self.assertEqual(self.calc.add(1000000, 2000000), 3000000)
        self.assertEqual(self.calc.subtract(5000000, 1000000), 4000000)
        self.assertEqual(self.calc.multiply(1000, 2000), 2000000)
        self.assertEqual(self.calc.divide(1000000, 1000), 1000)
        
        # Commutative property: a + b = b + a
        self.assertEqual(self.calc.add(5, 10), self.calc.add(10, 5))
        self.assertEqual(self.calc.add(-3, 7), self.calc.add(7, -3))
        self.assertEqual(self.calc.add(2.5, 3.1), self.calc.add(3.1, 2.5))
        
        # Commutative property: a * b = b * a
        self.assertEqual(self.calc.multiply(5, 10), self.calc.multiply(10, 5))
        self.assertEqual(self.calc.multiply(-3, 7), self.calc.multiply(7, -3))
        self.assertEqual(self.calc.multiply(2.5, 3.0), self.calc.multiply(3.0, 2.5))
        
        # Identity properties: a + 0 = a and a * 1 = a
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(-3, 0), -3)
        self.assertEqual(self.calc.add(2.5, 0), 2.5)
        
        self.assertEqual(self.calc.multiply(5, 1), 5)
        self.assertEqual(self.calc.multiply(-3, 1), -3)
        self.assertEqual(self.calc.multiply(2.5, 1), 2.5)
        
        # Zero properties: a * 0 = 0 and 0 / a = 0 (when a ≠ 0)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(-3, 0), 0)
        self.assertEqual(self.calc.multiply(2.5, 0), 0)
        
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(0, -3), 0)
        self.assertEqual(self.calc.divide(0, 2.5), 0)


if __name__ == '__main__':
    unittest.main()