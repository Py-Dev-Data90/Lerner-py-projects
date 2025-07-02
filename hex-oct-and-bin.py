# Let's start with the basics of number systems:
#So base 10 is 10 numbers, including zero, so 0-9. In the hexidecimal system, 0 is 1, 1 is 2, 2 is 3, etc etc up until 9, where it transfers to the alphabet. A is 10, B is 11, C is 12, D is 13, E is 14, F is 15
# IMPORTANT, In normal numbers, that is in base 10, means we have one stick of 10 and zero little cubes besides that. In base 16, this just means we have one stick of 16. We now have 16 cubes per stick rather than 10
# Decimal (Base 10) is the standard number system we use every day.
# It uses digits from 0 to 9. For example, the number 1234 means:
# (1 * 1000) + (2 * 100) + (3 * 10) + (4 * 1)

# Other number systems represent numbers with different bases:
# - Binary (Base 2): Only uses the digits 0 and 1. It's foundational for computing.
# - Octal (Base 8): Uses digits 0 through 7.
# - Hexadecimal (Base 16): Uses digits 0–9 and letters A–F (where A = 10, B = 11, ..., F = 15)

# HEXADECIMAL — Base 16
s = '10'
print(int(s, 16))  # Treats '10' as a hexadecimal value
# Explanation:
# Hexadecimal means each digit represents a power of 16.
# '10' in hex is (1 * 16^1) + (0 * 16^0) = 16 in decimal
# It's commonly used in computing, especially in memory addresses and color codes.

# DECIMAL — Base 10
s = '1234'
print(int(s))  # Interprets '1234' as a standard decimal number
# Since base 10 is the default, no need to specify the base

# OCTAL — Base 8
s = '1234'
print(int(s, 8))  # Interprets '1234' as octal
# In octal: 1234 = (1 * 8^3) + (2 * 8^2) + (3 * 8^1) + (4 * 8^0)
#           = 512 + 128 + 24 + 4 = 668 in decimal
# Octal was widely used in early computing systems and remains relevant in contexts like Unix file permissions

# BINARY — Base 2
s = '10101011'
print(int(s, 2))  # Interprets '10101011' as binary
# In binary: 
# (1 * 2^7) + (0 * 2^6) + (1 * 2^5) + (0 * 2^4) + (1 * 2^3) + (0 * 2^2) + (1 * 2^1) + (1 * 2^0)
# = 128 + 0 + 32 + 0 + 8 + 0 + 2 + 1 = 171 in decimal
# Binary is the core of digital computing; every bit is either a 0 or a 1, which corresponds to off/on states in hardware

# Summary:
# All these number systems allow you to represent and understand numbers in different contexts.
# Using int(s, base), Python lets you convert strings from any base to a standard decimal integer.
# These representations are especially useful in programming, data encoding, and understanding how computers store and process information.

#we have hex functions, hex() to convert an int