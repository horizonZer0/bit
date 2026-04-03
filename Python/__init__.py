# __init__.py

# Import the Bit function from your main logic file (bit.py)
from .bit import Bit

# This defines what is available when someone uses: from bit import *
__all__ = ['Bit']

# Optional: Add a version for your npm-style library
__version__ = "1.0.0"
__author__ = "deltaZer0"