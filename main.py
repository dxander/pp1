# main.py

from number_utils import identify_and_convert
from binary_utils import convert_to_binary

# I have added a comment to your code. Using the Fork feature at the top right

# Test values
#inputs = ["42", "0x2A", "0xFF"]
inputs = input("input either integer or hexadecimal starting with 0x: ")
kind, value = identify_and_convert(inputs)
binary = convert_to_binary(value)
print(f"Input: {inputs}, Type: {kind}, Decimal: {value}, Binary: {binary}")


