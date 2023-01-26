import operators as o

x1 = b'0000000100000001110000010101000001111100101010100101011100001110'

x2 = b'11001001'

def map_bin_to_hex(input):
    if (input == '0000'):
        return '0'
    elif (input == '0001'):
        return '1'
    elif (input == '0010'):
        return '2'
    elif (input == '0011'):
        return '3'
    elif (input == '0100'):
        return '4'
    elif (input == '0101'):
        return '5'
    elif (input == '0110'):
        return '6'
    elif (input == '0111'):
        return '7'
    elif (input == '1000'):
        return '8'
    elif (input == '1001'):
        return '9'
    elif (input == '1010'):
        return 'A'
    elif (input == '1011'):
        return 'B'
    elif (input == '1100'):
        return 'C'
    elif (input == '1101'):
        return 'D'
    elif (input == '1110'):
        return 'E'
    elif (input == '1111'):
        return 'F'
    else:
        print("FATAL EXCEPTION")

def map_hex_to_bin(input):
    if (input == '0'):
        return b'0000'
    elif (input == '1'):
        return b'0001'
    elif (input == '2'):
        return b'0010'
    elif (input == '3'):
        return b'0011'
    elif (input == '4'):
        return b'0100'
    elif (input == '5'):
        return b'0101'
    elif (input == '6'):
        return b'0110'
    elif (input == '7'):
        return b'0111'
    elif (input == '8'):
        return b'1000'
    elif (input == '9'):
        return b'1001'
    elif (input == 'A'):
        return b'1010'
    elif (input == 'B'):
        return b'1011'
    elif (input == 'C'):
        return b'1100'
    elif (input == 'D'):
        return b'1101'
    elif (input == 'E'):
        return b'1110'
    elif (input == 'F'):
        return b'1111'
    else:
        print("FATAL EXCEPTION")
    

def to_hex(x):
    hex_symbols = []
    i = 0
    temp = ''
    for x in x:
        temp +=str(x-48)
        i+=1
        if (i%4==0):
            hex_symbols.append(map_bin_to_hex(temp))
            temp = ''
  
    return 'hex\''+ ''.join(hex_symbols) + '\''


def from_hex(x):
    result = bytes()
    for x in x:
        result = o.CONCATENATE(result,map_hex_to_bin(x))
    
    return result