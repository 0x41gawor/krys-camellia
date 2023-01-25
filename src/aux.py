# Key derivation
# KL i KR mają mieć po 128bitów

from main import N_KEY_BITS
from operators import *

def KL_KR_derivation(K):
    KL = bytes()
    KR = bytes()
    if (N_KEY_BITS == 128): 
        KL = K
        KR = None
    if (N_KEY_BITS == 192): 
        KL = LEFT(K,128)
        KR = CONCATENATE(RIGHT(K,64),NOT(RIGHT(K,64)))
    if (N_KEY_BITS == 256):  
        KL = LEFT(K,128)
        KR = RIGHT(K,128)
    return KL, KR