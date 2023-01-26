from convert import *
from crypt import *
import sys


# Number of bits in the key 
N_KEY_BITS = 128

KEY =       from_hex('0AAABBB0011111100FFFFFF006969690') #128
# KEY =      from_hex('0AAABBB0011111100FFFFFF0069696900FFFFFF006969690') #192
# KEY =      from_hex('0AAABBB0011111100FFFFFF0069696900AAABBB0011111100FFFFFF006969690') #256



if __name__ == "__main__":
    # KEY = from_hex(sys.argv[1])
    # PLAINTEXT = from_hex(sys.argv[2])

    PLAINTEXT = 'moi ludzie dziecioly'
    print('PLAINTEXT: ascii\'' + PLAINTEXT + '\'')
    PLAINTEXT = from_ascii(PLAINTEXT)
    PLAINTEXT = from_hex(PLAINTEXT)
    CIPHERTEXT = encrypt(PLAINTEXT, KEY)
    print('CIPHERTEXT: ' + to_hex(CIPHERTEXT))
    PLAINTEXT = decrypt(CIPHERTEXT, KEY)
    PLAINTEXT = to_hex(PLAINTEXT)
    print('PLAINTEXT: '+ PLAINTEXT)
    PLAINTEXT = to_ascii(PLAINTEXT)
    print('PLAINTEXT: ' + PLAINTEXT)
