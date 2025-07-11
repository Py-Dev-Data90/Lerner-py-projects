# Floats aren't perfectly exact—this is one reason banks use specialized types like Decimal instead.
# We're starting with a string that *looks* like a number, but Python treats it as plain text.

x = '123.456'  # This is a string, not a number

# Trying to convert this string directly to an integer using int(x) won't work.
# Python will throw an error because the string contains a decimal point.
try:
    print("Trying int(x):", int(x))  # This line will crash
except ValueError:
    print("ValueError: Can't convert '123.456' directly to int because of the decimal.")

# Instead, we first convert the string to a float.
# Now Python sees it as the number 123.456.
float_value = float(x)

# Then, we convert that float to an int.
# This chops off (truncates) everything after the decimal point.
int_value = int(float_value)
print("After converting to float then int:", int_value)  # Output: 123

# If you'd prefer to round the number properly instead of just truncating,
# you can use the round() function.
rounded_value = round(float_value)
print("After rounding the float:", rounded_value)  # Output: 123 or 124 depending on the decimal


