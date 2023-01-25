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
    KW1 = o.LEFT(o.ROTATE(KL,0),4) # 4 -> 64
    KW2 = o.RIGHT(o.ROTATE(KL,0),4)

    K1 = o.LEFT(o.ROTATE(KA,0),4)
    K2 = o.RIGHT(o.ROTATE(KA,0),4)
    K3 = o.LEFT(o.ROTATE(KL,15),4)
    K4 = o.RIGHT(o.ROTATE(KL,15),4)
    K5 = o.LEFT(o.ROTATE(KA,15),4)
    K6 = o.RIGHT(o.ROTATE(KA,15),4)

    KL1 = o.LEFT(o.ROTATE(KA,30),4)
    KL2 = o.RIGHT(o.ROTATE(KA,30),4)

    K7 = o.LEFT(o.ROTATE(KL,45),4)
    K8 = o.RIGHT(o.ROTATE(KL,45),4)
    K9 = o.LEFT(o.ROTATE(KA,45),4)
    K10 = o.RIGHT(o.ROTATE(KL,60),4)
    K11 = o.LEFT(o.ROTATE(KA,60),4)
    K12 = o.RIGHT(o.ROTATE(KA,60),4)

    KL3 = o.LEFT(o.ROTATE(KL,77),4)
    KL4 = o.RIGHT(o.ROTATE(KL,77),4)

    K13 = o.LEFT(o.ROTATE(KL,94),4)
    K14 = o.RIGHT(o.ROTATE(KL,94),4)
    K15 = o.LEFT(o.ROTATE(KA,94),4)
    K16 = o.RIGHT(o.ROTATE(KA,94),4)
    K17 = o.LEFT(o.ROTATE(KL,111),4)
    K18 = o.RIGHT(o.ROTATE(KL,111),4)

    KW3 = o.LEFT(o.ROTATE(KL,111),4) 
    KW4 = o.RIGHT(o.ROTATE(KL,111),4)

elif (N_KEY_BITS == 192 |  N_KEY_BITS == 256): #12 # 16
    KW1 = o.LEFT(o.ROTATE(KL,0),4) # 4 -> 64
    KW2 = o.RIGHT(o.ROTATE(KL,0),4)

    K1 = o.LEFT(o.ROTATE(KB,0),4)
    K2 = o.RIGHT(o.ROTATE(KB,0),4)
    K3 = o.LEFT(o.ROTATE(KR,15),4)
    K4 = o.RIGHT(o.ROTATE(KR,15),4)
    K5 = o.LEFT(o.ROTATE(KA,15),4)
    K6 = o.RIGHT(o.ROTATE(KA,15),4)

    KL1 = o.LEFT(o.ROTATE(KR,30),4)
    KL2 = o.RIGHT(o.ROTATE(KR,30),4)

    K7 = o.LEFT(o.ROTATE(KB,30),4)
    K8 = o.RIGHT(o.ROTATE(KB,30),4)
    K9 = o.LEFT(o.ROTATE(KL,45),4)
    K10 = o.RIGHT(o.ROTATE(KL,45),4)
    K11 = o.LEFT(o.ROTATE(KA,45),4)
    K12 = o.RIGHT(o.ROTATE(KA,45),4)

    KL3 = o.LEFT(o.ROTATE(KL,60),4)
    KL4 = o.RIGHT(o.ROTATE(KL,60),4)

    K13 = o.LEFT(o.ROTATE(KR,60),4)
    K14 = o.RIGHT(o.ROTATE(KR,60),4)
    K15 = o.LEFT(o.ROTATE(KB,60),4)
    K16 = o.RIGHT(o.ROTATE(KB,60),4)
    K17 = o.LEFT(o.ROTATE(KL,77),4)
    K18 = o.RIGHT(o.ROTATE(KL,77),4)

    KL5 = o.LEFT(o.ROTATE(KA,77),4)
    KL6 = o.RIGHT(o.ROTATE(KA,77),4)

    K19 = o.LEFT(o.ROTATE(KR,94),4)
    K20 = o.RIGHT(o.ROTATE(KR,94),4)
    K21 = o.LEFT(o.ROTATE(KA,94),4)
    K22 = o.RIGHT(o.ROTATE(KA,94),4)
    K23 = o.LEFT(o.ROTATE(KL,111),4)
    K24 = o.RIGHT(o.ROTATE(KL,111),4)
        
    KW3 = o.LEFT(o.ROTATE(KB,111),4) 
    KW4 = o.RIGHT(o.ROTATE(KB,111),4)