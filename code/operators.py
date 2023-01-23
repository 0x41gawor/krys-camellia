def bitwise_and(x, y):
    result = x & y
    return bin(result)

def bitwise_or(x, y):
    result = x | y
    return bin(result)

def bitwise_xor(x, y):
    result = x ^ y
    return bin(result)

def logical_left_shift(x, y):
    result = x << y
    return bin(result)

def logical_right_shift(x, y):
    result = x >> y
    return bin(result)

def left_rotation(x, y):
    result = (x << y) | (x >> (32 - y))
    return bin(result)

def bitwise_complement(x):
    result = ~x
    return bin(result)

def hexadecimal_representation(x):
    return hex(x)