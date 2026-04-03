def Bit(value) -> str:
    """
    Converts a value (string, int, etc.) into its 8-bit binary representation.
    """
    # Convert input to string (handles Bit(123) without quotes)
    text = str(value)
    
    # ord(char) gets the ASCII value
    # format(x, '08b') converts to binary and pads to 8 bits
    return ' '.join(format(ord(char), '08b') for char in text)

# This defines what is exported when someone does 'from library import *'
__all__ = ['Bit']