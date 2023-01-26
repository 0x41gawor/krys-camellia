import operators as o

# This file contains code used for converting between our own types


# maps 4 bits to the hex symbol
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
# maps 1 hex symbol to string of 4 bits
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
    
# maps ascii symbol to corresponding hex representation
def map_ascii_to_hex(input):
    if (input == 'a'):
        return '61'
    elif (input == 'b'):
        return '62'
    elif (input == 'c'):
        return '63'
    elif (input == 'd'):
        return '64'
    elif (input == 'e'):
        return '65'   
    elif (input == 'f'):
        return '66'
    elif (input == 'g'):
        return '67'
    elif (input == 'h'):
        return '68'
    elif (input == 'i'):
        return '69'  
    elif (input == 'j'):
        return '6A'
    elif (input == 'k'):
        return '6B'
    elif (input == 'l'):
        return '6C'
    elif (input == 'm'):
        return '6D'  
    elif (input == 'n'):
        return '6E'
    elif (input == 'o'):
        return '6F'
    elif (input == 'p'):
        return '70'
    elif (input == 'q'):
        return '71'
    elif (input == 'r'):
        return '72'  
    elif (input == 's'):
        return '73'
    elif (input == 't'):
        return '74'
    elif (input == 'u'):
        return '75'
    elif (input == 'v'):
        return '76'  
    elif (input == 'w'):
        return '77'
    elif (input == 'x'):
        return '78'
    elif (input == 'y'):
        return '79'
    elif (input == 'z'):
        return '7A'
    elif (input == ' '):
        return '20'
    else:
        print("FATAL EXCEPTION")

# maps hex representation of an ascii symbol to ascii symbol
def map_hex_to_ascii(input):
    if (input == '61'):
        return 'a'
    elif (input == '62'):
        return 'b'
    elif (input == '63'):
        return 'c'
    elif (input == '64'):
        return 'd'
    elif (input == '65'):
        return 'e'   
    elif (input == '66'):
        return 'f'
    elif (input == '67'):
        return 'g'
    elif (input == '68'):
        return 'h'
    elif (input == '69'):
        return 'i'  
    elif (input == '6A'):
        return 'j'
    elif (input == '6B'):
        return 'k'
    elif (input == '6C'):
        return 'l'
    elif (input == '6D'):
        return 'm'  
    elif (input == '6E'):
        return 'n'
    elif (input == '6F'):
        return 'o'
    elif (input == '70'):
        return 'p'
    elif (input == '71'):
        return 'q'
    elif (input == '72'):
        return 'r'  
    elif (input == '73'):
        return 's'
    elif (input == '74'):
        return 't'
    elif (input == '75'):
        return 'u'
    elif (input == '76'):
        return 'v'  
    elif (input == '77'):
        return 'w'
    elif (input == '78'):
        return 'x'
    elif (input == '79'):
        return 'y'
    elif (input == '7A'):
        return 'z'  
    elif (input == '00'): # usuniecie paddingu
        return '' 
    elif (input == '20'):
        return ' '
    else:
        print("FATAL EXCEPTION")

# maps from our binary type to our hex type bin-->hex
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
  
    return 'hex\'' + ''.join(hex_symbols) + '\''
# maps from our hex type to our binary type
def from_hex(x):
    x = x[4:]
    x = x[:-1]
    result = bytes()
    for x in x:
        result = o.CONCATENATE(result,map_hex_to_bin(x))
    
    return result
# maps from our ascii type to our hex type
def from_ascii(x):
    hex_symbols = []
    for x in x:
        hex_symbols.append(map_ascii_to_hex(x))

    return 'hex\'' + ''.join(hex_symbols) + '\''
# maps from our hex type to our ascii type
def to_ascii(x):
    x = x[4:]
    x = x[:-1]
    length = len(x)
    i = 0
    result = ''
    while i < length-1:
        result += map_hex_to_ascii(x[i]+x[i+1])
        i += 2
    
    return 'ascii\'' + result + '\''