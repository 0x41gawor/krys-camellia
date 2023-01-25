#This code is a part of KeyScheduling process. That is why there will be KA,KB,KL and KR already provided. Hardcoding them for now.
#KL, KR, KA, KB - 128 bit -> 8
KL = b'00000000'
KR = b'11111111'
KA = b'00000000'
KB = b'11111111'

import core.operators as o
from input import N_KEY_BITS

#When rotation is bigger than length of the binary representation then it will do nothing. Just left/right shit.
if (N_KEY_BITS == 128): #8
    KW1 = o.LEFT(o.ROTATE(KL,0),64) # 4 -> 64
    KW2 = o.RIGHT(o.ROTATE(KL,0),64)

    K1 = o.LEFT(o.ROTATE(KA,0),64)
    K2 = o.RIGHT(o.ROTATE(KA,0),64)
    K3 = o.LEFT(o.ROTATE(KL,15),64)
    K4 = o.RIGHT(o.ROTATE(KL,15),64)
    K5 = o.LEFT(o.ROTATE(KA,15),64)
    K6 = o.RIGHT(o.ROTATE(KA,15),64)

    KL1 = o.LEFT(o.ROTATE(KA,30),64)
    KL2 = o.RIGHT(o.ROTATE(KA,30),64)

    K7 = o.LEFT(o.ROTATE(KL,45),64)
    K8 = o.RIGHT(o.ROTATE(KL,45),64)
    K9 = o.LEFT(o.ROTATE(KA,45),64)
    K10 = o.RIGHT(o.ROTATE(KL,60),64)
    K11 = o.LEFT(o.ROTATE(KA,60),64)
    K12 = o.RIGHT(o.ROTATE(KA,60),64)

    KL3 = o.LEFT(o.ROTATE(KL,77),64)
    KL4 = o.RIGHT(o.ROTATE(KL,77),64)

    K13 = o.LEFT(o.ROTATE(KL,94),64)
    K14 = o.RIGHT(o.ROTATE(KL,94),64)
    K15 = o.LEFT(o.ROTATE(KA,94),64)
    K16 = o.RIGHT(o.ROTATE(KA,94),64)
    K17 = o.LEFT(o.ROTATE(KL,111),64)
    K18 = o.RIGHT(o.ROTATE(KL,111),64)

    KW3 = o.LEFT(o.ROTATE(KL,111),64) 
    KW4 = o.RIGHT(o.ROTATE(KL,111),64)

elif (N_KEY_BITS == 192 |  N_KEY_BITS == 256): #12 # 16
    KW1 = o.LEFT(o.ROTATE(KL,0),64) # 4 -> 64
    KW2 = o.RIGHT(o.ROTATE(KL,0),64)

    K1 = o.LEFT(o.ROTATE(KB,0),64)
    K2 = o.RIGHT(o.ROTATE(KB,0),64)
    K3 = o.LEFT(o.ROTATE(KR,15),64)
    K4 = o.RIGHT(o.ROTATE(KR,15),64)
    K5 = o.LEFT(o.ROTATE(KA,15),64)
    K6 = o.RIGHT(o.ROTATE(KA,15),64)

    KL1 = o.LEFT(o.ROTATE(KR,30),64)
    KL2 = o.RIGHT(o.ROTATE(KR,30),64)

    K7 = o.LEFT(o.ROTATE(KB,30),64)
    K8 = o.RIGHT(o.ROTATE(KB,30),64)
    K9 = o.LEFT(o.ROTATE(KL,45),64)
    K10 = o.RIGHT(o.ROTATE(KL,45),64)
    K11 = o.LEFT(o.ROTATE(KA,45),64)
    K12 = o.RIGHT(o.ROTATE(KA,45),64)

    KL3 = o.LEFT(o.ROTATE(KL,60),64)
    KL4 = o.RIGHT(o.ROTATE(KL,60),64)

    K13 = o.LEFT(o.ROTATE(KR,60),64)
    K14 = o.RIGHT(o.ROTATE(KR,60),64)
    K15 = o.LEFT(o.ROTATE(KB,60),64)
    K16 = o.RIGHT(o.ROTATE(KB,60),64)
    K17 = o.LEFT(o.ROTATE(KL,77),64)
    K18 = o.RIGHT(o.ROTATE(KL,77),64)

    KL5 = o.LEFT(o.ROTATE(KA,77),64)
    KL6 = o.RIGHT(o.ROTATE(KA,77),64)

    K19 = o.LEFT(o.ROTATE(KR,94),64)
    K20 = o.RIGHT(o.ROTATE(KR,94),64)
    K21 = o.LEFT(o.ROTATE(KA,94),64)
    K22 = o.RIGHT(o.ROTATE(KA,94),64)
    K23 = o.LEFT(o.ROTATE(KL,111),64)
    K24 = o.RIGHT(o.ROTATE(KL,111),64)
        
    KW3 = o.LEFT(o.ROTATE(KB,111),64) 
    KW4 = o.RIGHT(o.ROTATE(KB,111),64)