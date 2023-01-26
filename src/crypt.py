from crypt_block import *

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


def encrypt(plaintext, key):
    plaintext_blocks = get_128bit_blocks(plaintext)
    ciphertext = b''
    for i in plaintext_blocks:
        ciphertext += encrypt_block(i, key)
    return ciphertext


def decrypt(ciphertext, key):
    ciphertext_blocks = get_128bit_blocks(ciphertext)
    plaintext = b''
    for i in ciphertext_blocks:
        plaintext += decrypt_block(i, key)
    return plaintext