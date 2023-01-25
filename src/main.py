from hex_to_bin import *
from lib import *
import sys


# Number of bits in the key 
N_KEY_BITS = 128

KEY =      from_hex('0AAABBB0011111100FFFFFF006969690') #128
# KEY =      from_hex('0AAABBB0011111100FFFFFF0069696900FFFFFF006969690') #192
# KEY =      from_hex('0AAABBB0011111100FFFFFF0069696900AAABBB0011111100FFFFFF006969690') #256
PLAINTEX = from_hex('00001111000011110000111100001111')



if __name__ == "__main__":
    # KEY = from_hex(sys.argv[1])
    # PLAINTEX = from_hex(sys.argv[2])
    KL, KR = KL_KR_derivation(KEY)
    KA, KB = KA_KB_generation(KL, KR)
    print(KA)
    print(KB)

