# The name of the file is silly but the meaning is a follows: Common_part('encrypt', 'decrypt')
from lib import *

def encrypt_block(PLAINTEXT, KEY):

    KL, KR = KL_KR_derivation(KEY)
    KA, KB = KA_KB_generation(KL, KR)
    if (N_KEY_BITS == 128):
        keys = subkeys_generation_128(KL, KR, KA, KB)
    elif (N_KEY_BITS == 192 or  N_KEY_BITS == 256):
        keys = subkeys_generation_192_256(KL, KR, KA, KB)

    if (N_KEY_BITS == 128):
        (KW1, KW2, K1, K2, K3, K4, K5, K6, KL1, KL2, K7, K8, K9, K10, K11, K12, KL3, KL4, K13, K14, K15, K16, K17, K18, KW3, KW4) = keys
    elif (N_KEY_BITS == 192 or  N_KEY_BITS == 256):
        (KW1, KW2, K1, K2, K3, K4, K5, K6, KL1, KL2, K7, K8, K9, K10, K11, K12, KL3, KL4, K13, K14, K15, K16, K17, K18, KL5, KL6, K19, K20, K21, K22, K23, K24, KW3, KW4) = keys

    # Key pre-whitening
    D1 = XOR(LEFT(PLAINTEXT,64), KW1)
    D2 = XOR(RIGHT(PLAINTEXT, 64), KW2)
    # 1-st Feistel block
    keys = (K1, K2, K3, K4, K5, K6)
    D1, D2 = feistel_block(CONCATENATE(D1,D2), keys)
    # FL and FL-1
    D1 = FL_function(D1, KL1)
    D2 = FL1_function(D2, KL2)
    # 2-nd Feistel block
    keys = (K7, K8, K9, K10, K11, K12)
    D1, D2 = feistel_block(CONCATENATE(D1,D2), keys)
    # FL and FL-1
    D1 = FL_function(D1, KL3)
    D2 = FL1_function(D2, KL4)
    # 3-rd Feistel block
    keys = (K13, K14, K15, K16, K17, K18)
    D1, D2 = feistel_block(CONCATENATE(D1,D2), keys)

    # Additional 4-th Feistel Block for 192/256 N_KEY_BITS option
    if (N_KEY_BITS == 192 or  N_KEY_BITS == 256):
        D1 = FL_function(D1, KL5)
        D2 = FL1_function(D2, KL6)
        keys = (K19, K20, K21, K22, K23, K24)
        D1, D2 = feistel_block(CONCATENATE(D1,D2), keys)
    
    temp = D1
    D1 = XOR(D2, KW3)
    D2 = XOR(temp, KW4)

    CIPHERTEXT = CONCATENATE(D1,D2)
    return CIPHERTEXT

def decrypt_block(CIPHERTEXT, KEY):

    KL, KR = KL_KR_derivation(KEY)
    KA, KB = KA_KB_generation(KL, KR)
    if (N_KEY_BITS == 128):
        keys = subkeys_generation_128(KL, KR, KA, KB)
    elif (N_KEY_BITS == 192 or  N_KEY_BITS == 256):
        keys = subkeys_generation_192_256(KL, KR, KA, KB)


    def invert_128(keys):
        (KW1, KW2, K1, K2, K3, K4, K5, K6, KL1, KL2, K7, K8, K9, K10, K11, K12, KL3, KL4, K13, K14, K15, K16, K17, K18, KW3, KW4) = keys
        return (KW3, KW4, K18, K17, K16, K15, K14, K13, KL4, KL3, K12, K11, K10, K9, K8, K7, KL2, KL1, K6, K5, K4, K3, K2, K1, KW1, KW2)

    def invert_192_256(keys):
        (KW1, KW2, K1, K2, K3, K4, K5, K6, KL1, KL2, K7, K8, K9, K10, K11, K12, KL3, KL4, K13, K14, K15, K16, K17, K18, KL5, KL6, K19, K20, K21, K22, K23, K24, KW3, KW4) = keys
        return (KW3, KW4, K24, K23, K22, K21, K20, K19, KL6, KL5, K18, K17, K16, K15, K14, K13, KL4, KL3, K12, K11, K10, K9, K8, K7, KL2, KL1, K6, K5, K4, K3, K2, K1, KW1, KW2)

    if (N_KEY_BITS == 128):
        (KW1, KW2, K1, K2, K3, K4, K5, K6, KL1, KL2, K7, K8, K9, K10, K11, K12, KL3, KL4, K13, K14, K15, K16, K17, K18, KW3, KW4) = invert_128(keys)
    elif (N_KEY_BITS == 192 or  N_KEY_BITS == 256):
        (KW1, KW2, K1, K2, K3, K4, K5, K6, KL1, KL2, K7, K8, K9, K10, K11, K12, KL3, KL4, K13, K14, K15, K16, K17, K18, KL5, KL6, K19, K20, K21, K22, K23, K24, KW3, KW4) = invert_192_256(keys)

    # Key pre-whitening
    D1 = XOR(LEFT(CIPHERTEXT,64), KW1)
    D2 = XOR(RIGHT(CIPHERTEXT, 64), KW2)
    # 1-st Feistel block
    keys = (K1, K2, K3, K4, K5, K6)
    D1, D2 = feistel_block(CONCATENATE(D1,D2), keys)
    # FL and FL-1
    D1 = FL_function(D1, KL1)
    D2 = FL1_function(D2, KL2)
    # 2-nd Feistel block
    keys = (K7, K8, K9, K10, K11, K12)
    D1, D2 = feistel_block(CONCATENATE(D1,D2), keys)
    # FL and FL-1
    D1 = FL_function(D1, KL3)
    D2 = FL1_function(D2, KL4)
    # 3-rd Feistel block
    keys = (K13, K14, K15, K16, K17, K18)
    D1, D2 = feistel_block(CONCATENATE(D1,D2), keys)

    # Additional 4-th Feistel Block for 192/256 N_KEY_BITS option
    if (N_KEY_BITS == 192 or  N_KEY_BITS == 256):
        D1 = FL_function(D1, KL5)
        D2 = FL1_function(D2, KL6)
        keys = (K19, K20, K21, K22, K23, K24)
        D1, D2 = feistel_block(CONCATENATE(D1,D2), keys)
    
    temp = D1
    D1 = XOR(D2, KW3)
    D2 = XOR(temp, KW4)

    PLAINTEXT = CONCATENATE(D1,D2)
    return PLAINTEXT

