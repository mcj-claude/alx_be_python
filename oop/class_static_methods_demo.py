class Calculator:
    """
    Calculator class demonstrating static methods and class methods.
    """
    # Class attribute that will be accessed by the class method
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """
        Static method that returns the sum of two numbers.
        Static methods don't have access to class or instance attributes.
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """
        Class method that returns the product of two numbers.
        Class methods have access to class attributes via the cls parameter.
        Prints the calculation_type class attribute before performing multiplication.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b