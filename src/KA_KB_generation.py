#MOCK OF F FUNCTION
def F(a,b): 
    return a

import core.operators as o
from input import N_KEY_BITS

KL = b'00000000'
KR = b'11111111'
sigma1 = b'0000'
sigma2 = b'0001'
sigma3 = b'0010'
sigma4 = b'0100'
sigma5 = b'1000'
sigma6 = b'1001'

KA = bytes()
KB = bytes()

#purple section
D1 = o.LEFT(o.XOR(KL,KR),4)
D2 = o.RIGHT(o.XOR(KL,KR),4)
D2 = o.XOR(D2,F(D1, sigma1))
D1 = o.XOR(D1,F(D2, sigma2))
#blue section
D1 = o.XOR(D1, o.LEFT(KL, 4))
D2 = o.XOR(D2, o.RIGHT(KL, 4))
D2 = o.XOR(D2, F(D1, sigma3))
D1 = o.XOR(D1, F(D2, sigma4))
KA = o.CONCATENATE(D1, D2)
#yellow section
if (N_KEY_BITS==192 or N_KEY_BITS==256):
    D1 = o.LEFT(o.XOR(KA, KR), 4)
    D2 = o.RIGHT(o.XOR(KA, KR), 4) 
    D2 = o.XOR(D2, F(D1, sigma5))
    D1 = o.XOR(D1, F(D2, sigma6))
    KB = o.CONCATENATE(D1, D2)


print(KA)
print(KB)



