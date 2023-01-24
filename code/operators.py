# from the given two vectors, creates a new one as the result of AND operation bit by bit
def AND(x, y):
   return bytes(a & b for a, b in zip(x, y))
# from the given two vectors, creates a new one as the result of OR operation bit by bit#######
def OR(x, y):
    return bytes(a | b for a, b in zip(x, y))
# from the given vector, creates a new one as the result of XOR operation bit by bit
def NOT(x):
    return bytes(a ^ 1 for a in x)
# from the given two vectors, creates a new one as the result of XOR operation bit by bit
def XOR(x, y):
    return bytes(((a|b) & (~(a&b)) ) for a, b in zip(x, y))
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



print('Input bytes')
a = b'00001111'
b = b'00110011'
print(f'a: {a}')
print(f'b: {b}')
print("x = AND(a,b)")
x = AND(a,b)
print(f'x: {x}')
print("x = OR(a,b)")
x = OR(a,b)
print(f'x: {x}')
print("x = XOR(a,b)")
x = XOR(a,b)
print(f'x: {x}')
print("x = LEFT(a,4)")
x = LEFT(a,4)
print(f'x: {x}')
print("x = LEFT(b,4)")
x = LEFT(b,4)
print(f'x: {x}')
print("x = RIGHT(a,4)")
x = RIGHT(a,4)
print(f'x: {x}')
print("x = RIGHT(b,4)")
x = RIGHT(b,4)
print(f'x: {x}')
print("x = CONCATENATE(a,b)")
x = CONCATENATE(a,b)
print(f'x: {x}')
print("x = NOT(a)")
x = NOT(a)
print(f'x: {x}')
print("x = NOT(b)")
x = NOT(b)
print(f'x: {x}')
print("x = ROTATE(a,2)")
x = ROTATE(a,3)
print(f'x: {x}')