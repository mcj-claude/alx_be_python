def safe_divide(numerator, denominator):
    """
    Performs division with robust error handling.
    
    Args:
        numerator: The number to be divided
        denominator: The number to divide by
        
    Returns:
        str: Result message indicating success or error
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        den = float(denominator)
        
        # Attempt division
        result = num / den
        return f"The result of the division is {result}"
        
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."