# Defines base operations on our own binary type, these operations are obtained from 'docs/KRYS_PROJEKT_CAMELLIA.pdf/' section 2.2

# from the given two vectors, creates a new one as the result of AND operation bit by bit
def AND(x, y):
   return bytes(a & b for a, b in zip(x, y))
# from the given two vectors, creates a new one as the result of OR operation bit by bit
def OR(x, y):
    return bytes(a | b for a, b in zip(x, y))
# from the given two vectors, creates a new one as the result of XOR operation bit by bit
def XOR(x, y):
    res = bytes(a ^ b for a, b in zip(x, y))
    return ''.join([format(x, 'b') for x in res]).encode('ascii')
# from the given vector, creates a new one as the result of XOR operation bit by bit
def NOT(x):
    return bytes(a ^ 1 for a in x)
# returns `n` most-left bits from `x` vector
def LEFT(x, n):
    return x[:n]
# returns `n` most-right bits from `x` vector
def RIGHT(x, n):
    return x[(len(x)-n):]
# joins two vector together, end of `x` with begining of `y`
def CONCATENATE(x, y):
    return x + y
# rotates vector `x` by `n` positions to the LEFT
def ROTATE(x, n):
   return x[n:]+x[:n]
