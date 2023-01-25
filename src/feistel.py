#MOCK OF F FUNCTION
def F(a,b): 
    return a

import core.operators as o


k1 = b'0000'
k2 = b'0000'
k3 = b'0000'
k4 = b'0000'
k5 = b'0000'
k6 = b'0000'
keys = (k1, k2, k3, k4, k5, k6)

D1D2 = b'00001111'
# does the 6 round of Feistel Cipher on the given input (D1D2 input) 
# as input 6-element tuple of keys is accepted
def feistel_block(D1D2, keys):
    D1 = o.LEFT(D1D2,4)
    D2 = o.RIGHT(D1D2,4)
    (k1, k2, k3, k4, k5, k6) = keys

    # 1-st round
    D1 = D1
    D2 = o.XOR(D2, F(D1,k1))
    # 2-nd round
    D1 = o.XOR(D1, F(D2,k2))
    D2 = D2
    # 3-rd round
    D1 = D1
    D2 = o.XOR(D2, F(D1, k3))
    # 4-th round
    D1 = o.XOR(D1, F(D2, k4))
    D2 = D2
    # 5-th round
    D1 = D1
    D2 = o.XOR(D2, F(D1, k5))
    # 6-th round
    D1 = o.XOR(D1, F(D2, k6))
    D2 = D2

    return o.CONCATENATE(D1,D2)

print(feistel_block(D1D2, keys))