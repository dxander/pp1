def identify_and_convert(user_input):
    """Identify if the input is an integer or hex and convert to decimal."""
    if user_input.startswith("0x") or user_input.startswith("0X"):
        decimal_value = int(user_input, 16)
        return "hexadecimal", decimal_value
    else:
        decimal_value = int(user_input)
        return "integer", decimal_value
