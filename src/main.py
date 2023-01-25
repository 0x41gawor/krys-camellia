from hex_to_bin import *
from crypt_block import *
import sys


# Number of bits in the key 
N_KEY_BITS = 128

KEY =       from_hex('0AAABBB0011111100FFFFFF006969690') #128
# KEY =      from_hex('0AAABBB0011111100FFFFFF0069696900FFFFFF006969690') #192
# KEY =      from_hex('0AAABBB0011111100FFFFFF0069696900AAABBB0011111100FFFFFF006969690') #256
PLAINTEXT = from_hex('00001111000011110000111100001111')


if __name__ == "__main__":
    # KEY = from_hex(sys.argv[1])
    # PLAINTEXT = from_hex(sys.argv[2])
    print(to_hex(PLAINTEXT))
    CIPHERTEXT = encrypt_block(PLAINTEXT, KEY)
    print(to_hex(CIPHERTEXT))
    PLAINTEXT = decrypt_block(CIPHERTEXT, KEY)
    print(to_hex(PLAINTEXT))