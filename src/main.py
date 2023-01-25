from hex_to_bin import *
from crypt_block import *
import sys


# Number of bits in the key 
N_KEY_BITS = 128

KEY =       from_hex('0AAABBB0011111100FFFFFF006969690') #128
# KEY =      from_hex('0AAABBB0011111100FFFFFF0069696900FFFFFF006969690') #192
# KEY =      from_hex('0AAABBB0011111100FFFFFF0069696900AAABBB0011111100FFFFFF006969690') #256
PLAINTEXT = from_hex('00001111000011110000111100001111000011110000111100001111000011110AAABBB0011111100FFFFFF00696AABDF')



# as the name suggest, includes padding
def get_128bit_blocks(TEXT):
    text_blocks = []
    import math
    loops_count = math.ceil(len(TEXT) / 128)

    for i in range(loops_count-1):
        text_blocks.append(LEFT(TEXT, 128))
        TEXT = TEXT[128:]

    for i in range(128-len(TEXT)):
        TEXT += b'0'
    
    text_blocks.append(TEXT)

    return text_blocks


if __name__ == "__main__":
    # KEY = from_hex(sys.argv[1])
    # PLAINTEXT = from_hex(sys.argv[2])

    # print(to_hex(PLAINTEXT))
    # CIPHERTEXT = encrypt_block(PLAINTEXT, KEY)
    # print(to_hex(CIPHERTEXT))
    # PLAINTEXT = decrypt_block(CIPHERTEXT, KEY)
    # print(to_hex(PLAINTEXT))
    plaintext_blocks = get_128bit_blocks(PLAINTEXT)
    print(plaintext_blocks)