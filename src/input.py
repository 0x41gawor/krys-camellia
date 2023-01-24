# Number of bits in the key 
# Attenzione: select the appriopriate key below
N_KEY_BITS = 256

# KEY = b'01001100' #128
# KEY = b'010011001111' #192
KEY = b'0100110011110000' #256


# dla uproszczenia robie tak, ze 64bity prawdziewe to się równa 4 u nas w kodziku (to tak narazie, żeby łatwo się developowało)
# 64 => 4
# 128 => 8
# 192 => 12
# 256 => 16