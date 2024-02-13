decimal_string = "112 105 99 111 67 84 70 123 112 49 76 76 102 51 114 51 100 95 100 97 116 97 95 118 49 97 95 115 116 51 103 48 125"

# Split string into list of decimal values
decimal_list = list(map(int, decimal_string.split()))

# Convert decimal values to ASCII characters
ascii_string = ''.join(chr(decimal) for decimal in decimal_list)

print(ascii_string)
