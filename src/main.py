from hex_to_bin import *
from lib import *
import sys


# Number of bits in the key 
N_KEY_BITS = 256

# KEY =      from_hex('0AAABBB0011111100FFFFFF006969690') #128
# KEY =      from_hex('0AAABBB0011111100FFFFFF0069696900FFFFFF006969690') #192
KEY =      from_hex('0AAABBB0011111100FFFFFF0069696900AAABBB0011111100FFFFFF006969690') #256
PLAINTEX = from_hex('00001111000011110000111100001111')



if __name__ == "__main__":
    # KEY = from_hex(sys.argv[1])
    # PLAINTEX = from_hex(sys.argv[2])
    KL, KR = KL_KR_derivation(KEY)
    KA, KB = KA_KB_generation(KL, KR)
    if (N_KEY_BITS == 128):
        temp = (KW1, KW2, K1, K2, K3, K4, K5, K6, KL1, KL2, K7, K8, K9, K10, K11, K12, KL3, KL4, K13, K14, K15, K16, K17, K18, KW3, KW4) = subkeys_generation_128(KL, KR, KA, KB)
    elif (N_KEY_BITS == 192 or  N_KEY_BITS == 256):
        temp = (KW1, KW2, K1, K2, K3, K4, K5, K6, KL1, KL2, K7, K8, K9, K10, K11, K12, KL3, KL4, K13, K14, K15, K16, K17, K18, KL5, KL6, K19, K20, K21, K22, K23, K24, KW3, KW4) = subkeys_generation_192_256(KL, KR, KA, KB)
    print(temp)