import core.operators as o

from input import KEY
from input import N_KEY_BITS

# Key derivation
# KL i KR mają mieć po 128bitów
K = KEY
KL = bytes()
KR = bytes()
if (N_KEY_BITS == 128): #8
    KL = K
    KR = None
if (N_KEY_BITS == 192): #12
    KL = o.LEFT(K,8)
    KR = o.CONCATENATE(o.RIGHT(K,4),o.NOT(o.RIGHT(K,4)))
if (N_KEY_BITS == 256): #16 
    KL = o.LEFT(K,8)
    KR = o.RIGHT(K,8)

print(f'KL: {KL}')
print(f'KR: {KR}')